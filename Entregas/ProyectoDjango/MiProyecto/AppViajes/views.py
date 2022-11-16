from django.shortcuts import render
from django.http import HttpResponse
from .models import Agencia, Viajero, Tour
from .forms import CrearTourForm, CrearAgenciaForm, CrearViajeroForm

# Create your views here.
def mostrar_index(request):

    return render(request, 'index.html')

"""
def mostrar_tours(request):

    return render(request, 'tours.html')


def mostrar_viajeros(request):

    return render(request, 'viajeros.html')

 def mostrar_agencias(request):

    return render(request, 'agencias.html')    """

#-------------- Funciones de Creación ---------------------    

def crear_agencia(request):

    if request.method == 'POST':

        formulario = CrearAgenciaForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            agencia = Agencia(nombre=formulario_limpio['nombre'], responsable=formulario_limpio['responsable'], email=formulario_limpio['email'], telefono=formulario_limpio['telefono'])

            agencia.save()

            return render(request, 'index.html')

    else:
        formulario = CrearAgenciaForm()

    return render(request, 'crear_agencia.html', {'formulario': formulario}) 

def crear_tour(request):

    if request.method == 'POST':

        formulario = CrearTourForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            tour = Tour(nombre=formulario_limpio['nombre'], precio=formulario_limpio['precio'], capacidad=formulario_limpio['capacidad'])

            tour.save()

            return render(request, 'index.html')

    else:
        formulario = CrearTourForm()

    return render(request, 'crear_tour.html', {'formulario': formulario}) 

def crear_viajero(request):

    if request.method == 'POST':

        formulario = CrearViajeroForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            viajero = Viajero(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], email=formulario_limpio['email'])

            viajero.save()

            return render(request, 'index.html')

    else:
        formulario = CrearViajeroForm()

    return render(request, 'crear_viajero.html', {'formulario': formulario}) 

#--- Funciones de Búsqueda----

def buscar_agencia(request):

    if request.GET.get('nombre', False): 
        nombre = request.GET['nombre']
        agencia = Agencia.objects.filter(nombre__icontains=nombre)

        return render(request, 'buscar_agencia.html', {'agencia': agencia})
    else:
        respuesta = 'No hay datos'
    return render(request, 'buscar_agencia.html', {'respuesta': respuesta})