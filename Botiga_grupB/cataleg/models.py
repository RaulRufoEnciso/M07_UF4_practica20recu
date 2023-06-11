from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)
    precio = models.IntegerField()
    estado = models.BooleanField()
    fabricante = models.CharField(max_length=30)

