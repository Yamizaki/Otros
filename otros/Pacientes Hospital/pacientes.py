
import os
import time
#Mensaje de bienvenida
print("*" * 30)
print(" Hola bienvenido al S.A.P.")
print("*" * 30)


#Menu de decision principal 
desicion=int(input("""Escoge una opcion:
1.- Agregar paciente nuevo
2.- Buscar paciente por nombre
3.- Ver lista de pacientes 
4.- Salir 
                """))

#Lista donde se agregan sujetos
lista_pacientes=[]


while desicion != 4:
    #Tarea 1
    if desicion == 1:
        nombre_paciente = input(str("Ingresa el nombre del  paciente: "))
        # edad_paciente= input(int("Ingresa la edad del paciente:"))
        # obser_paciente= input(str("Ingresa las observacion del paciente:"))
        lista_pacientes.append(nombre_paciente)
        os.system("cls")
        print(f"Agregando a {nombre_paciente} a la base de datos... \n espere por favor")
        time.sleep(3)
        print("*" * 30)
        print(" Paciente agregado con exito")
        print("*" * 30)
        
        desicion=int(input("""Escoge una opcion:
        1.- Agregar paciente nuevo
        2.- Buscar paciente por nombre
        3.- Ver lista de pacientes 
        4.- Salir 
                """))
        

    #Tarea 2
    if desicion == 2:
        busqueda = input(str("Ingrese el nombre del paciente que busca: "))
        if busqueda in lista_pacientes:
            print("*" * 30)
            print(f"Se encontro al paciente {busqueda}")
            print("*" * 30)
           
            time.sleep(5)
            os.system("cls")
            desicion=int(input("""Escoge una opcion:
        1.- Agregar paciente nuevo
        2.- Buscar paciente por nombre
        3.- Ver lista de pacientes 
        4.- Salir 
                """))
            
        else:
            print("*" * 30)
            print("No se encontro a nadie con ese nombre")
            print("*" * 30)
            
            time.sleep(3)
            os.system("cls")
            desicion=int(input("""Escoge una opcion:
        1.- Agregar paciente nuevo
        2.- Buscar paciente por nombre
        3.- Ver lista de pacientes 
        4.- Salir 
                """))

    #Tarea 3
    if desicion == 3:
        print(lista_pacientes)
        
        time.sleep(5)
        desicion=int(input("""Escoge una opcion:
1.- Agregar paciente nuevo
2.- Buscar paciente por nombre
3.- Ver lista de pacientes 
4.- Salir 
                """))



