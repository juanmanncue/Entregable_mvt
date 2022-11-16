from django.db import models

# Create your models here.
#Clase Tour, gestion los datos para cada paseo.
class Tour(models.Model):

    nombre = models.CharField(max_length=40) #Nombre del Tour
    precio = models.FloatField()
    capacidad=models.IntegerField() #Cantidad de personas admitidas al tour

#Clase Viajero, gestion de datos de las personas.
class Viajero(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

#Clase Agencia, gestion de datos de las Agencias que ofrecen los paseos.
class Agencia(models.Model):

    nombre = models.CharField(max_length=40)
    responsable = models.CharField(max_length=40)
    email = models.EmailField()
    telefono=models.IntegerField(null=True)
    
