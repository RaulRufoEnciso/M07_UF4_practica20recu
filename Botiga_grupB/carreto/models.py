from django.db import models
from cataleg.models import Productos

# Create your models here.
class Carrito(models.Model):
    productoId = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    comprado = models.BooleanField(default=False)
