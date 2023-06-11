from django.db import models

class Comanda(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    comprado = models.BooleanField(default=False)

  
