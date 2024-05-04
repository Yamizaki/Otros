
#importar librerias
from importlib.resources import read_text
import os
import sys
from pathlib import Path

#  #Saludo de bienvenida 
os.system("cls")
nombre = str(input("Ingresa tu nombre: \n"))
print("*" *50)
print(f"      Hola, {nombre}, bienvenido a tu recetario!")
print("*" *50)
#Direccion donde estan ubicadas las carpetas
ruta= os.getcwd()
carpetas= os.listdir()
print(f"El recetario se encuentra en la siguiente direccion: \n {ruta}")


#Indicar el numero de recetas
numero_recetas=0 
for txt in Path(ruta).glob("**/*.txt"):
    numero_recetas +=1
print(f"*****  Tienes un total de {numero_recetas} recetas  *****")

#Menu de eleccion "1-6"
opcion="zzz"
while (opcion.isalpha()):
    print("Escoge una opcion del 1 al 6...")
    opcion=(input("""
                INGRESA UNA OPCION:
                1.- Leer receta
                2.- Crear receta
                3.- Crear categoria
                4.- Eliminar receta
                5.- Eliminar categoria
                6.- SALIR
                """))  
 
# 1  Leer Receta 
#     Elegir categoria 
def categorias():
    for carpCategorias in carpetas:
        if not carpCategorias.endswith(".py"):
            print(carpCategorias)   
    print("Escribe el nombre de tu receta: ")
    global cat 
    cat = str(input())
    os.system("cls")       
    return cat.capitalize()

#     Mostrar recetas
def recetas(catEleg):
    for archirecetas in (os.listdir(catEleg)):
        print(archirecetas)
    global recetaSeleccionada
    recetaSeleccionada = str(input("Escoge una receta para leer..."))
    return recetaSeleccionada  

#     Elegir receta (leer)

def leerReceta(categ,recet): 
    recetaParaLeer = Path(f"{ruta}\\{categ}\\{recet}.txt")
    leido = open(recetaParaLeer)
    print(leido.read())



  
#2  Crear receta
    # Elegir categoria 
def categorias():
    for carpCategorias in carpetas:
        if not carpCategorias.endswith(".py"):
            print(carpCategorias)   
    print("Escribe el nombre de tu receta: ")
    global cat 
    cat = str(input())
    os.system("cls")       
    return cat.capitalize()
    # Crear documento.txt
def crearReceta(categ):
    nombreReceta=input("Ingresa el nombre de tu nueva receta...")
    nuevaReceta=open(Path(f"{ruta}\\{categ}\\{nombreReceta}+.txt"),"w")
    contenidoReceta=input("Ingresa el contenido de tu nueva receta...")
    nuevaReceta.write(f"{contenidoReceta}") 
    # Crear contenido receta
 
#3  Crear categoria 
    #Elegir nombre de la categoria 
    #Crear categoria 
def crearCategoria():
    nombre=input("Ingresa el nombre de la nueva categoria...")
    os.mkdir(nombre)
    
   
#4  Eliminar receta  
    #Elegir categoria 
def eliminarReceta():
    catEl=input("Ingresa el nombre de la categoria...")
    recEliminar=input("Ingresa el nombre de la categoria que deseas eliminar...")
    os.remove(f"{catEl}\\{recEliminar}.txt")
    #Mostrar recetas
    #Eleminar receta
    
#5   Eliminar categoria
    #Elegir categoria
def eliminarCategoria():
    catEliminar=input("Ingresa el nombre de la categoria que deseas eliminar...")
    os.remove(catEliminar)
    #Eliminar dicha categoria 
    
#69 Finaliza programa

def menu_1():
        recetas(categorias())
        leerReceta(cat,recetaSeleccionada)
def menu_2():
        categorias()    
        crearReceta(cat)
def menu_3():
        crearCategoria()
def menu_4():
        eliminarReceta() 
def menu_5():
        eliminarCategoria()  
        
        
             
#**************************TODOS LOS MENUS**************************

if opcion == "1":
    menu_1()   
elif opcion == "2":
    menu_2()
elif opcion == "3":       
    menu_3()
        
elif opcion == "4":        
    menu_4()
        
elif opcion == "5":
    menu_5()
        
else: 
    sys.exit()