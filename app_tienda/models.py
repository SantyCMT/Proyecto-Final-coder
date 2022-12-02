from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    nombre_usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    
    
class Cafe(models.Model):
    nombre_cafe =  models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 100)
    
class Torta(models.Model):
    nombre_torta = models.CharField(max_length = 50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 100)
