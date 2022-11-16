"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import mostrar_index, crear_agencia, crear_tour, crear_viajero, buscar_agencia

urlpatterns = [
    # path('mostrar_agencias/', mostrar_agencias, name='Agencias'), FALTA INCLUIR EL IMPORT
    #path('mostrar_tours/', mostrar_tours, name='Tours'), FALTA INCLUIR EL IMPORT
    #path('mostrar_viajeros/', mostrar_viajeros, name='Viajeros'), FALTA INCLUIR EL IMPORT
    path('', mostrar_index),
    path('crear_agencia/',crear_agencia,name='Nueva Agencia'),
    path('crear_tour/', crear_tour, name='Nuevo Tour'),
    path('crear_viajero/',crear_viajero, name='Nuevo Viajero'),
    path('buscar_agencia/',buscar_agencia, name='Buscar Agencia')
    
]