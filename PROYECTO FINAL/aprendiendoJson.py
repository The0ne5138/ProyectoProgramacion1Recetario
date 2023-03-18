contenido=" \n \n Este es el contenido de mi archivo. \nCreado con Python."
archivo = open("PROYECTO FINAL/prueba.txt",'a')
archivo.write(contenido)
varias_lineas = ["Esta es una linea\n","Esta es otra linea\n", "Y esta la ultima agregada."]
archivo.writelines(varias_lineas)
archivo.close()

#******************************************************************************************
import json
# escribe en recetario.json en formato json el contenido de dicRecetario. (ya lo hicimos).
#with open("PROYECTO FINAL/recetario.json",'w') as archivo:
   # json.dump(dicRecetario,archivo)

# Ahora usamos el arichibo json para las funciones de buscqueda por ejemplo.
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

with open("PROYECTO FINAL/recetario.json") as archivo:  # abre el archivo json en recetario.
   recetario = json.load(archivo)                       # y o usamos como diccionario.

#print(type(recetario))
#print(busca_receta("Anchi",recetario))
#print(busca_receta("pizza",recetario))
#print(recetario["Anchi"][0][1])

#****************************Cargamos ingredeintes en el dic***********************************************
def carga_ingrediente():
    """Metodo que ingresa UN ingrediente. Devuelve una lista de tres elemntos 'Ingrediente, cantidad, unidad'."""
    lista=[]
    nombre = input("Ingrese Nombre del ingrediente:  ")
    lista.append(nombre)
    unidad = input(" Ingrese 1 si la unidad es Gramos (gs) \n Ingrese 2 si la unidad es Kilogramos (Kg) \n Ingrese 3 si la unidada es Litros (Lts) \n Ingrese 4 si la unidad es mililitros (mm) \n Ingrese 5 si este ingrediente no presisa unidad. \n Ingrese 6 el ingrediente no tiene unidad \n Ingrese 7 si el ingrediente se expresa en unidades ")
    lista.append(unidad)
    cantidad = input(f"Ingrese Cantidad de {nombre}:  ")
    lista.append(cantidad)
    return lista

def carga_ingrdientes(clave, diccionario):
    """ Agrega toda la lista de N-ingredintes al diccionario."""
    lista=[]
    opcion=1
    # opcion=input("Oprima 1 si desea ingresar un nuveo ingrediente. \n Oprima 0 si ya no va a ingresar otro ingrediente.")
    while opcion==1:
        opcion=int(input("Oprima 1 si desea ingresar un nuveo ingrediente. \n Oprima 0 si ya no va a ingresar otro ingrediente."))
        if opcion==1:
            lista.append(carga_ingrediente())
        elif opcion==0:
            print("Lista de ingredientes finaliados.")
        else:
            print("Ingreso erroneo, intente nuevamente.")
            opcion=1
    diccionario[clave][0]=lista

    with open("PROYECTO FINAL/recetario.json",'w') as archivo:  #Guardo el contenido de archivo (py) en en archivo.JSON
        json.dump(diccionario,archivo)



#recetario["prueba"][0].insert(0,carga_ingrdientes("prueba", recetario))
carga_ingrdientes("Prueba", recetario)
print(recetario["Prueba"])






