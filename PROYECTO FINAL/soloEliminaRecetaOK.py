# Abriremos el recetario, buscaremos alguna receta. y si la encontramos 
# la eliminamos del diccionario(recetario).

import json

def busca_receta(clave,diccionario):
    """ retorna un dicconario con un elemento clave/valor, si es que lo encuentra y sino lo encetra avia de este echo"""
    bandera = 0
    for i in diccionario:
        if ( i == clave):
          #eturn print({clave:diccionario[clave]})
          bandera = 1
          break
    if bandera == 1:
      return True
    else: return False

with open("PROYECTO FINAL/recetario2deprueba.json") as archivo:  # abre el archivo json en recetario.
   recetario = json.load(archivo)                                # y o usamos como diccionario.

def elimina_receta(clave, diccionario):
    """ Dada una clave y un diccionario, elimina el par clave/valor del diccionario temporal, pero no del arvhivo .JSON"""
    if busca_receta(clave, diccionario):
        del diccionario[clave]
    else:
        print("Receta no existente en el Recetario.")

elimina_receta("Anchi",recetario)

with open("PROYECTO FINAL/recetario2deprueba.json",'w') as archivo:  #Guardo el contenido de archivo (py) en en archivo.JSON
        json.dump(recetario, archivo)

for i in recetario:
   print(i)
