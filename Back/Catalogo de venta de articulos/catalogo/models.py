from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    talla=models.CharField(max_length=5)
    foto=models.ImageField(upload_to='catalogo/images', null=True, blank=True)
    color=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre