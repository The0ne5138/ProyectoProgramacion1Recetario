# Funcion que cargara todas las caracteristicas de una receta. 

import json

def crea_receta(diccionario):
    """ Solicita todos los datos de una receta, y devuelve un par clave/valor para luego agregar al diccionario-recetario"""
    nombre = input("Ingrese el nombre de la receta: ")
    carga_ingredientes(nombre,diccionario)
    carga_preparacion(nombre,diccionario)
    carga_imagenes(nombre, diccionario) # Falta hacer: creo que para hacerla en tkinter.
    preparacion = input(f"Ingrese el tiempo de preparacion de la receta:{nombre}")
    diccionario[nombre][3] = preparacion  # posicion 3 es donde se guardan los tiempos de preparacion.
    coccion = input(f"Ingrese el tiempo de coccion de la receta:{nombre}")
    diccionario[nombre][4] = coccion  # posicion 3 es donde se guardan los tiempos de preparacion.
    diccionario[nombre][5]=fecha_creacion()
    # diccionario[clave][5] = nuevofecha o fecha de modificacion.