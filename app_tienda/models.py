from django.db import models

# Create your models here.

class Cafe(models.Model):
    nombre_cafe =  models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.nombre_cafe} Precio: {self.precio}"

class Torta(models.Model):
    nombre_torta = models.CharField(max_length = 50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.nombre_torta} Precio: {self.precio} "
        
 

class Bebidas(models.Model):
    nombre_bebida = models.CharField(max_length = 100)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_bebida} Precio: {self.precio}"


class Salados(models.Model):
    nombre_salados = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_salados} Precio: {self.precio}"



class Panqueques_Wafles(models.Model):
    nombre_PW = models.CharField(max_length= 100)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_PW} Precio: {self.precio}"



