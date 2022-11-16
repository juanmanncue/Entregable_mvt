from django import forms

class CrearAgenciaForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)
    responsable = forms.CharField(max_length=40)
    email = forms.EmailField()
    telefono = forms.IntegerField()


class CrearViajeroForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    

class CrearTourForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)
    precio = forms.FloatField()
    capacidad = forms.IntegerField()
    