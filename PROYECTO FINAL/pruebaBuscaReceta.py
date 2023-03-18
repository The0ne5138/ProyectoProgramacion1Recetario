dicRecetario = {"Galletas Cookies": [[["Harina", 400, "gs"], ["Manteca", 200, "gs"], ["Azúcar comun", 180, "gs"],  # Ingredientes
                                      ["Azúcar mascabo", 200, "gs"], [
                                          "Esencia de vainilla", "C/N", ""],
                                      ["Sal", 15, "gs"], ["Polvo de hornear",
                                                          5, "gs"], ["Chocolate", 300, "gs"]
                                      ],                                                                           # Preparacion
                                     [["Paso 1: Mezclar con batidor o batidora de mano la manteca en cubos a temperatura ambiente, los azúcares, la sal y el polvo de hornear. "],
                                      ["Paso 2: Mezclar los huevos y la vainilla."],
                                      ["Paso 3: Mezclar la harina con el chocolate picado y agregar todo a la preparación anterior."],
                                      ["Paso 4: Poner la masa, de a cucharadas en una placa enmantecada o con papel manteca y llevarlas a heladera durante 20 minutos."],
                                      ["Paso 5: Cocinarlas por 15 o 20 minutos. Al sacarlas del horno, aplastarlas un poco para que queden más compactas."],
                                      ["Paso 6: Dejar enfriar en rejilla."]
                                      ],
                                     "imagenes pueden o no estar",  # Imagenes
                                     50,  # Tiempo de preparacion
                                     20,  # Tiempo de coocion
                                     " 09/03/22 "  # Fecha de creacion.
                                     ],
                "Anchi": [[["Semola", 500, "gs"], ["Azucar", 250, "gs"], ["Cascara de limon", "C/", ""], ["Clavo de olor", "C/N", ""],
                           ["Pelon deshidratado", "C/N", ""]],
                          [["Paso 1: En una olla con agua (aproximadamente tres litros) ir agregando la sémola de maíz (polenta); lo ideal es arrojarla en forma de lluvia. El agua debe estar hirviendo y hay que mezclar de manera constante. El tiempo de mezclado va a depender de la cantidad de polenta que agreguemos."],
                           ["Paso 2: A la mezcla le sumamos el azúcar y la rama de canela o clavo de olor."],
                           ["Paso 3: Con la polenta cocida, podemos agregar la cáscara de limón. Va a depender del criterio de cada uno. La cáscara de los cítricos puede usarse de forma rallada."],
                           ["Paso 4: Si agrega los pelones deshidratados, dejarlos en remojo toda una noche y hacerlos hervir antes de incorporarlos a la preparación. Hervir una media hora más. Retirar del fuego, la consistencia debe ser semi-líquida. Dejar enfriar y agregar hielo."]
                           ],
                          "imagenes pueden o no estar",
                          30,
                          60,
                          " 09/03/22 "
                          ],
                "Prueba": [[], [], "", None, None, None]
                }


def busca_receta(clave, diccionario):
    """ retorna un dicconario con un elemento clave/valor, si es que lo encuentra y sino lo encetra avia de este echo"""
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
# ****************************************************************************************************************
# print(busca_receta("Anchi",dicRecetario))
# print()
# print(busca_receta("Galletas Cookies",dicRecetario))
# rint()
# print(busca_receta("prueba",dicRecetario))
# print()
# print(busca_receta("Pitza",dicRecetario))

# **********************************************************************************************************
def carga_ingrediente():
    """Funcion que ingresa UN ingrediente. Devuelve una lista de tres elemntos 'Ingrediente, cantidad, unidad'."""
    lista = []
    nombre = input("Ingrese Nombre del ingrediente:  ")
    lista.append(nombre)
    unidad = input(" Ingrese 1 si la unidad es Gramos (gs) \n Ingrese 2 si la unidad es Kilogramos (Kg) \n Ingrese 3 si la unidada es Litros (Lts) \n Ingrese 4 si la unidad es mililitros (mm) \n Ingrese 5 si este ingrediente no presisa unidad. \n Ingrese 6 el ingrediente no tiene unidad \n Ingrese 7 si el ingrediente se expresa en unidades ")
    lista.append(unidad)
    cantidad = input(f"Ingrese Cantidad de {nombre}:  ")
    lista.append(cantidad)
    return lista
# ********************************************************************************************************************


def carga_ingrdienteS(clave, diccionario):
    """ Agrega toda la lista de N-ingredintes al diccionario."""
    lista = []
    opcion = 1
    # opcion=input("Oprima 1 si desea ingresar un nuveo ingrediente. \n Oprima 0 si ya no va a ingresar otro ingrediente.")
    while opcion == 1:
        opcion = int(input(
            "Oprima 1 si desea ingresar un nuveo ingrediente. \n Oprima 0 si ya no va a ingresar otro ingrediente."))
        if opcion == 1:
            lista.append(carga_ingrediente())
        elif opcion == 0:
            print("Lista de ingredientes finaliados.")
        else:
            print("Ingreso erroneo, intente nuevamente.")
            opcion = 1
    diccionario[clave][0] = lista


carga_ingrdienteS("Prueba", dicRecetario)
print(dicRecetario["Prueba"])
