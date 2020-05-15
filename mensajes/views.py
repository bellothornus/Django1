from django.shortcuts import render
from django.http import HttpResponse
from mensajes.models import Comentario
# Create your views here.

def comentario(request):
    if request.method=="POST":
        com=Comentario(nombre=request.POST['nombre'],asunto=request.POST['asunto'],comentario=request.POST.get('comentario'))
        com.save()
        return render(request, "comentarios.html", {"gracias":"Gracias por enviar su comentario!"})
    return render(request, "comentarios.html")

def index(request):
    return render(request, "index.html")