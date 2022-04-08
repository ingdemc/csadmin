from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Soporte(models.Model):
    id=models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField(max_length=254)
    detalleserror = models.CharField(max_length=500)

    fechacreacion = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name ='Soporte'
        verbose_name ='Soportes'

    def __str__(self):
        return "{0}-{1}".format(self.nombre,self.apellido)