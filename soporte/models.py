from django.db import models
from django.utils import timezone

class Soporte(models.Model):
    id=models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField(max_length=254)
    detalleserror = models.CharField(max_length=500)
    fechacreacion = models.DateTimeField(default=timezone.now)