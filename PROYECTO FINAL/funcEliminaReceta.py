# Funcion que recibe una clave busca y elimina reeta de un dic
# Necesita un dic para modificarlo

def eliminaReceta(clave, diccionario):
    if busca_receta(clave,diccionario):
        del diccionario[clave]
    else: 
        print("Receta no existente en el Recetario.")
       
