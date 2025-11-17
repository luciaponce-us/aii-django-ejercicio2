from django.db import models

class Partido(models.Model):
    local = models.CharField(max_length=100)
    visitante = models.CharField(max_length=100)
    goles_local = models.IntegerField(default=0)
    goles_visitante = models.IntegerField(default=0)
    jornada = models.ForeignKey('Jornada', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} en Jornada {self.jornada}"
  

class Temporada(models.Model):
    anyo = models.IntegerField()

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    fundacion = models.IntegerField(default=1950)
    estadio = models.CharField(max_length=100)
    aforo = models.IntegerField(default=100)
    direccion = models.CharField(max_length=100)
    
class Jornada(models.Model):
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    numero = models.IntegerField()
    fecha = models.CharField(max_length=100)