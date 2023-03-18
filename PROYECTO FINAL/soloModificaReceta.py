import json

def modifica_receta(diccionario):
    """ Modifica receta, debera llamar a otros metodos/funciones segun la eleccion de modificacion del usuario"""
    #print("Ingrese 1 si quiere modificar el nombre")   No se como modificar solo una clave de un diccionario /opcion/ podria reemplazar clve-valor  solo cambiando clave.
    clave=input("Ingrese el nombre de la receta que desee modificar.")  # O se puede mostrar una lista desplegable con todas las recetas guardadas en el recetario.
    if not(busca_receta(clave,diccionario)):
        print("Receta no encontrada.")
    else:
        print("Ingrese 1 si quiere modificar ingredientes")    #Lama a metodo MODIFICA INGREDIENTE/s
        print("Ingrese 2 si quiere modificar la preparacion")  # Llama a la funcion modifica preparacion.
        print("Ingrese 3 si quiere modificar las imagenes")
        print("Ingrese 4 si quiere modificar el tiempo de preparacion")
        print("Ingrese 5 si quiere modificar el tiempo de coccion")
        opcion = int(input(" Ingrese 6 si quiere modificar fecha de creacion: ")) # creo q esto no deberia porder modificarse.
        #lista = diccionario[clave]
        #if opcion == 1: 
        #lista[0]= input("Ingrese el nuevo nombre para la receta.")
        if opcion == 1:
            modifica_ingredientes(clave,diccionario)
        elif opcion == 2:
            carga_preparacion(clave, diccionario)
        elif opcion == 3:
            carga_imagenes(clave, diccionario) # Falta hacer: creo que para hacerla en tkinter.
        elif opcion == 4:
            nuevoTiempo = input(f"Ingrese el nuevo tiempo de preparacion de la receta:{clave}")
            diccionario[clave][3] = nuevoTiempo  # posicion 3 es donde se guardan los tiempos de preparacion.
        elif opcion == 5:
             nuevoTiempo = input(f"Ingrese el nuevo tiempo de coccion de la receta:{clave}")
             diccionario[clave][4] = nuevoTiempo  # posicion 3 es donde se guardan los tiempos de preparacion.
        elif opcion == 7:
            print("NO SE puede modificar la fecha de creacion por que ya no seria creacion, ahora seria FECHA DE MODIFICACION xD")
            # diccionario[clave][5] = nuevofecha o fecha de modificacion.

def modifica_ingredientes(clave, diccionario):
    """ Muestra lo ingredientes y pregunta cual quiere modificar, lo modifica guarda los cambios. """
    lista= diccionario[clave][0]
    print("Los ingredientes a modificar son: ")
    for i in lista:
        print(f"Oprima {i} si dese modificar el ingrediente: {clave[i]}")
    eleccion = int(input("Escriba su eleccion: "))   
    diccionario[clave][0][eleccion]= carga_ingrediente()     

def carga_preparacion(clave, diccionario):
    """ Solicitara un nuevo paso de la receta mientas el usuario avise que se quiere cargar uno mas."""
    opcion = 1
    pasos=[]
    i=0
    while opcion == 1 :
        i=i+1
        paso=input("Ingrese el paso numero {i}")+"\n"
        pasos.append(paso)
        opcion=input("Ingrese 1 si qiere ingrese un paso mas.\n Ingrese 0 si ya no va a ingresar pasos de la receta. ")
    diccionario[clave][1]= pasos



