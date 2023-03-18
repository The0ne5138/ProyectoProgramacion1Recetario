import json
from datetime import date
from datetime import datetime

def crea_receta(diccionario):
    """ Solicita todos los datos de una receta, y devuelve un par clave/valor para luego agregar al diccionario-recetario"""
    nombre = input("Ingrese el nombre de la receta: ")
    nombre = nombre.lower()
    receta = [[],[],None,None,None,None]
    diccionario[nombre]=receta
    carga_ingredienteS(nombre,diccionario)
    carga_preparacion(nombre,diccionario)
    # carga_imagenes(nombre, diccionario) # Falta hacer: creo que para hacerla en tkinter.
    # diccionario[clave][2]= "imagenes"
    preparacion = input(f"Ingrese el tiempo de preparacion de la receta:{nombre}")
    diccionario[nombre][3] = preparacion  # posicion 3 es donde se guardan los tiempos de preparacion.
    coccion = input(f"Ingrese el tiempo de coccion de la receta:{nombre}")
    diccionario[nombre][4] = coccion  # posicion 3 es donde se guardan los tiempos de preparacion.
    diccionario[nombre][5]=fecha_creacion()

#**************************************************************************
def modifica_receta(diccionario):
    """ Modifica receta, debera llamar a otros metodos/funciones segun la eleccion de modificacion del usuario"""
    #print("Ingrese 1 si quiere modificar el nombre")   No se como modificar solo una clave de un diccionario /opcion/ podria reemplazar clve-valor  solo cambiando clave.
    clave = input("Ingrese el nombre de la receta que desee modificar.")  # O se puede mostrar una lista desplegable con todas las recetas guardadas en el recetario.
    clave = clave.lower()
    if not(busca_receta(clave,diccionario)):
        print("Receta no encontrada.")
    else:
        print("Ingrese 1 si quiere modificar ingredientes")    #Lama a metodo MODIFICA INGREDIENTE/s
        print("Ingrese 2 si quiere modificar la preparacion")  # Llama a la funcion modifica preparacion.
        print("Ingrese 3 si quiere modificar las imagenes")
        print("Ingrese 4 si quiere modificar el tiempo de preparacion")
        print("Ingrese 5 si quiere modificar el tiempo de coccion")
        print(" Ingrese 6 si quiere modificar fecha de creacion: ") # creo q esto no deberia porder modificarse.
        opcion = int(input("Ingrese su eleccion: "))
        #lista = diccionario[clave]
        #if opcion == 1: 
        #lista[0]= input("Ingrese el nuevo nombre para la receta.")
        if opcion == 1:
            modifica_ingredientes(clave,diccionario)
        elif opcion == 2:
            carga_preparacion(clave, diccionario)
        elif opcion == 3:
            pass
            #carga_imagenes(clave, diccionario) # Falta hacer: creo que para hacerla en tkinter.
            # diccionario[clave][2]= "imagenes"
        elif opcion == 4:
            nuevoTiempo = input(f"Ingrese el nuevo tiempo de preparacion de la receta:{clave}")
            diccionario[clave][3] = nuevoTiempo  # posicion 3 es donde se guardan los tiempos de preparacion.
        elif opcion == 5:
             nuevoTiempo = input(f"Ingrese el nuevo tiempo de coccion de la receta:{clave}")
             diccionario[clave][4] = nuevoTiempo  # posicion 3 es donde se guardan los tiempos de preparacion.
        elif opcion == 7:
            print("NO SE puede modificar la fecha de creacion por que ya no seria creacion, ahora seria FECHA DE MODIFICACION xD")
            # diccionario[clave][5] = nuevofecha o fecha de modificacion.

#**************************************************************************
def elimina_receta(clave, diccionario):
    """ Dada una clave y un diccionario, elimina el par clave/valor del diccionario temporal, pero no del arvhivo .JSON"""
    if busca_receta(clave, diccionario):
        del diccionario[clave]
    else:
        print("Receta no existente en el Recetario.")

# **********************************************************************************************************
def carga_ingrediente():
    """Funcion que ingresa UN ingrediente. Devuelve una lista de tres elemntos 'Ingrediente, cantidad, unidad'."""
    lista = []
    nombre = input("Ingrese Nombre del ingrediente:  ")
    nombre = nombre.lower()
    lista.append(nombre)
    unidad = int(input("Ingrese 1 si la unidad es Gramos (gs) \nIngrese 2 si la unidad es Kilogramos (Kg) \nIngrese 3 si la unidada es Litros (Lts) \nIngrese 4 si la unidad es mililitros (mm) \nIngrese 5 si este ingrediente no presisa unidad. \nIngrese 6 si el ingrediente se expresa en unidades "))
    lista.append(unidad)
    cantidad = int(input(f"Ingrese Cantidad de {nombre}:  "))
    lista.append(cantidad)
    return lista

# ********************************************************************************************************************
def carga_ingredienteS(clave, diccionario):
    """ Agrega toda la lista de N-ingredintes al diccionario."""
    lista = []
    opcion = 1
    # opcion=input("Oprima 1 si desea ingresar un nuveo ingrediente. \n Oprima 0 si ya no va a ingresar otro ingrediente.")
    while opcion == 1:
        opcion = int(input("Oprima 1 si desea ingresar un nuveo ingrediente. \n Oprima 0 si ya no va a ingresar otro ingrediente."))
        if opcion == 1:
            lista.append(carga_ingrediente())
        elif opcion == 0:
            print("Lista de ingredientes finaliados.")
        else:
            print("Ingreso erroneo, intente nuevamente.")
            opcion = 1
    diccionario[clave][0] = lista

#**************************************************************************
def busca_receta(clave, diccionario):
    """ Retorna un dicconario con un elemento clave/valor, si es que lo encuentra y sino lo encetra avia de este echo"""
    bandera = 0
    for i in diccionario:
        if (i == clave):
            # eturn print({clave:diccionario[clave]})
            bandera = 1
            break
    if bandera == 1:
        return True
    else:
        return False

#**************************************************************************
    
def modifica_ingredientes(clave, diccionario):
    """ Muestra lo ingredientes y pregunta cual quiere modificar, lo modifica guarda los cambios. """
    lista= diccionario[clave][0]
    print("Los ingredientes a modificar son: ")
    for i in lista:
        print(f"Oprima {i} si dese modificar el ingrediente: {clave[i]}")
    eleccion = int(input("Escriba su eleccion: "))   
    diccionario[clave][0][eleccion]= carga_ingrediente()     

#**************************************************************************
def carga_preparacion(clave, diccionario):
    """ Solicitara un nuevo paso de la receta mientas el usuario avise que se quiere cargar uno mas."""
    opcion = 1
    pasos=[]
    i=0
    while opcion == 1 :
        i=i+1
        paso=input(f"Ingrese el paso numero {i}")+"\n"
        pasos.append(paso)
        opcion=int(input("Ingrese 1 si qiere ingrese un paso mas.\nIngrese 0 si ya no va a ingresar pasos de la receta. "))
    diccionario[clave][1] = pasos  

#**************************************************************************

def fecha_creacion():
    """ Retorna un str que contiene la fecha actual """
    hoy = date.today()
    return f"{hoy.day}/{hoy.month}/{hoy.year}"

#******************************* FIN DE LAS FUNCIONES ********************************************

#******************************* Menu principal ********************************************

def menuPrincipal(diccionario):
    """ En este menu se eligira entre: Cargar, Modificar y Eliminar una receta."""
    eleccion = 1    
    while eleccion == 1:
            eleccion=int(input("Ingrese 1 si quiere cargar una nueva receta. \nIngrese 2 si quiere Modificar una receta. \nIngrese 3 si quiere eliminar una receta. \nIngrese 0 si dese terminar. "))
            if eleccion == 1:
                crea_receta(diccionario)
            elif eleccion == 2:
                modifica_receta(diccionario)
                eleccion = 1
            elif eleccion == 3:
                clave = input("Ingrese el nombre de la receta que desea eliminar. ")
                elimina_receta(clave,diccionario)
                eleccion = 1
            elif eleccion == 0:
                break    
            else:
                print("Ingreso erroneo, intente nuevamente.")
                eleccion = 1
    

#******************************* Ejemplo de aplicacion *******************************************

# recetario={}
with open("PROYECTO FINAL/recetario2deprueba.json") as archivo:  # abre el archivo json en recetario.
   recetario = json.load(archivo)                                # y lo usamos como diccionario.

menuPrincipal(recetario)   ## LLAMADA AL MENU PRINCIPAL
    
with open("PROYECTO FINAL/recetario2deprueba.json",'w') as archivo:  #Guardo el contenido de archivo recetario(py) en un archivo.JSON
        json.dump(recetario,archivo)
                   