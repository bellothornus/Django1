from django.db import models

#Create your models here.


class Post(models.Model):
    autor=models.CharField(max_length=20)
    asunto=models.CharField(max_length=30)
    post=models.TextField()

class Comentario(models.Model):
    nombre=models.CharField(max_length=15)
    asunto=models.CharField(max_length=30)
    comentario=models.TextField()
    id_post=models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)

#comment = Comentario(nombre="Prueba", asunto="Pues yo creo que la solucion es esta", comentario="blablablablabla",id_post="1")