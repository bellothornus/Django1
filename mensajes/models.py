from django.db import models

#Create your models here.

class Comentario(models.Model):
    nombre=models.CharField(max_length=15)
    asunto=models.CharField(max_length=30)
    comentario=models.TextField()