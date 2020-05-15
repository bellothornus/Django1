from django.shortcuts import render
from django.http import HttpResponse
from mensajes.models import Comentario, Post
# Create your views here.

def comentario(request):
    if request.method=="POST":
        com=Comentario(nombre=request.POST['nombre'],asunto=request.POST['asunto'],comentario=request.POST.get('comentario'))
        com.save()
        return render(request, "comentarios.html", {"gracias":"Gracias por enviar su comentario!"})
    return render(request, "comentarios.html")

def index(request):
    query = Post.objects.all()
    return render(request, "index.html", {"posts":query})

def post_id(request,id):
    query_post = Post.objects.get(id=id)
    query_comment = Comentario.objects.filter(id_post=id)

    if request.method=="POST":
        post=Post.objects.get(id=request.POST['post_id'])
        com=Comentario(nombre=request.POST['nombre'],asunto=request.POST['asunto'],comentario=request.POST.get('comentario'),id_post=post)
        com.save()
        return render(request, "base.html", {"post":query_post,"comentarios":query_comment, "gracias":"Gracias por enviar su comentario!"})
    else:
        return render(request, "base.html", {"post":query_post,"comentarios":query_comment})