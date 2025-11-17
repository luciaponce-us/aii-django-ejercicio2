"""
URL configuration for futbol project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from partidos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio,name='inicio'),
    path('ultimaTemporada/', views.ultima_temporada, name='ultima_temporada'),
    path('equipos/', views.equipos, name='equipos'),
    path('equipos/equipo/<int:id>', views.detalle_equipo, name='equipo'),
    path('estadiosMayores/', views.estadios_mas_aforo, name='estadios_mayores'),
    path('cargar/', views.cargar, name='cargar')
]
