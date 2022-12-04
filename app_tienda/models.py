from django.db import models

# Create your models here.

class Cafe(models.Model):
    nombre_cafe =  models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 100)
    
class Torta(models.Model):
    nombre_torta = models.CharField(max_length = 50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 100)
