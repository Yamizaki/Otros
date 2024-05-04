from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

# Create your views here.

def index(request):
    
    return render (request, "index.html")

def catalagoProductos(request):
    productos=Producto.objects.all()
    return render (request, "catalogo.html", {
        'producto': productos,
    })
    print(productos)

