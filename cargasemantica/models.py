from statistics import correlation
from django.db import models
from django.utils import timezone

#  Create your models here.
class Metadatos(models.Model):
    id = models.AutoField(primary_key=True)
    aliasconxion = models.CharField(max_length=30)
    comentariobd =models.TextField(max_length=150)
    nomhost = models.CharField(max_length=10)
    nompuerto = models.IntegerField()
    nombd = models.CharField(max_length=20)
    usuario = models.CharField(max_length=30)
    passw = models.CharField(max_length=25)
    fechacreacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{0}-{1}".format(self.aliasconxion,self.nombd)