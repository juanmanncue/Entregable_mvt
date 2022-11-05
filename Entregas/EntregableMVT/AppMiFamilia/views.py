from django.shortcuts import render
from .models import Familiar

# Create your views here.

def mostrar_info (request):

    madre = Familiar(nombre='Maria', fecha_nacimiento='24/08/1983',edad=39)
    hijo = Familiar(nombre='José', fecha_nacimiento='12/05/2013',edad=9)
    hija = Familiar(nombre='Eugenia', fecha_nacimiento='15/01/2015',edad=7)

    return render(request,'mostrar_info.html', {'objetos': [madre, hijo, hija]})

