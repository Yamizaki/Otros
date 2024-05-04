from django.shortcuts import render
from django.http import HttpResponse
from .models import Pelicula
from .models import Director
# Create your views here.

def index(request):
    return render(request, "index.html")

def directores(request):
    var_pelicula= Director.objects.all()
    return render(request, "directores.html", {
        'var_dir':var_pelicula
    })

def pelicula(request, id):
    var_pelicula2= Pelicula.objects.filter(director_pelicula=id)
    
    return render(request, "pelicula.html", {
        'var_dir':var_pelicula2
    })

def resumen(request, id):
    var_pelicula3= Pelicula.objects.filter(id=id)
    print(var_pelicula3)
    return render(request, "resumen.html", {
        'var_dir':var_pelicula3
    })
    
    