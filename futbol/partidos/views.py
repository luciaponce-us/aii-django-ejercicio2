from django.shortcuts import render

from .models import *

def inicio(request):
    # Obtener temporadas
    temporadas = Temporada.objects.all().order_by('-año')
    return render(request, 'partidos/inicio.html', {'temporadas': temporadas})

def ultima_temporada(request):
    # Obtener jornadas y sus partidos de la última temporada
    return render(request, 'partidos/ultima_temporada.html')

def equipos(request):
    
    return render(request, 'partidos/equipos.html')

def detalle_equipo(request, equipo_id):
    return render(request, 'partidos/detalle_equipo.html')

def estadios_mas_aforo(request):
    return render(request, 'partidos/estadios_mas_aforo.html')

def cargar(request):
    return render(request, 'partidos/cargar.html')