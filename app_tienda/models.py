from django.db import models

# Create your models here.

class Cafe(models.Model):
    nombre_cafe =  models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.nombre_cafe} | Precio: {self.precio}"

class Torta(models.Model):
    nombre_torta = models.CharField(max_length = 50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.nombre_torta} | Precio: {self.precio}"
 