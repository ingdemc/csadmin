from statistics import correlation
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#  Create your models here.
class Metadatos(models.Model):
    id = models.AutoField(primary_key=True)
    iduser= models.ForeignKey(User, on_delete=models.CASCADE)
    aliasconxion = models.CharField(max_length=30)
    comentariobd =models.TextField(max_length=150)
    nomhost = models.CharField(max_length=100)
    nompuerto = models.IntegerField()
    nombd = models.CharField(max_length=80)
    usuario = models.CharField(max_length=100)
    passw = models.CharField(max_length=150)
    fechacreacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{0}-{1}".format(self.aliasconxion,self.nombd)

class schema_gr(models.Model):
    id_m = models.AutoField(primary_key=True)
    id_schema = models.ForeignKey(Metadatos, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img", max_length=None, null=True)
    
    def __str__(self):
        return "{0}".format(self.id_schema)
   