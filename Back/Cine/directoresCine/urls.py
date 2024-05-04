from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('directores/', views.directores),
    path('directores/<int:id>', views.pelicula),
    path('directores/pelicula/resumen/<int:id>', views.resumen)
]