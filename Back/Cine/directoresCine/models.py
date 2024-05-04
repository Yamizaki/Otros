from django.db import models

# Create your models here.

class Director(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    director_pelicula= models.ForeignKey(Director, on_delete=models.CASCADE)
    nombre_pelicula= models.CharField(max_length=50)
    resumen= models.CharField(max_length=500)

    def __str__(self):
        return self.nombre_pelicula

