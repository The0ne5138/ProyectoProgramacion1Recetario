class receta:
    """ Vamos a describir metodos y atributos para representar una receta."""
    def __init__(self, nombre):
        self.nombre=nombre
        self.ingredientes           # Es una clase independiente? o sublclase?
        self.preparacion
        self.imagenes
        self.tiempo_preparacion
        self.fecha_de_creacion

    def crear_receta(self): # se pediran los datos para crear la nueva receta.
        """ Crea una nueva receta y la guarda en la lista de recetas."""
        self.nombre = input("Ingrese nombre de la receta.")
        self.ingredientes = self.ingresa_ingrediente()
        self.preparacion = input("Describa las instrucciones para la preparacion de la receta.")
        #self.imagenes = # Aun no se como hacer ingresar imagenes.
        self.tiempo_preparacion = input("Ingrese el tiempo que sera necesario para preparar esta receta.")
        #self.fecha_de_creacion = # Algun metoto para ingresar la fecha automaticamente el dia que se crea la receta. Con las modificaciones de receta no se cambia la fecha?
        print(f"Felicidades la receta: {self.nombre} a sido guardada exitosamente.") # listo, receta guardada.

    def modifica_receta(self,receta): # Elegir entre pasar el nombre por parametro, o que el metodo de opciones para buscar y eliminar.""se pasa un objeto RECETA"".
        """ Busca segun eleccion de una lista o parametro pasado. luego modifica y guarda los cambios """
        receta_aux = busca_receta(receta)
        return # listo receta modificada con exito.

    def eliminar_receta(self, receta):  # Elegir entre pasar el nombre por parametro, o que el metodo de opciones para buscar y eliminar.
        """ Busca y Elimina una receta de acuerdo al nombre pasado como parametro"""
        # aplicar metodo para para buscar una receta.

    def busca_receta(self,receta): # Preguntar por que criterio de busqueda quiere aplicar el usuario.
        """ Pregunta al usuario por que criterio quiere buscar y retorna la receta buscada ( o un indice para ubicar receta)"""
        return # Retorna una receta o un indice para ubicar la receta.
    
    def ingresa_ingrediente(self): # El metodo puede solicitar los datos de ingredientes mostrando una lista de opciones. o 
                                   # puede recibi losd datos pasados como parametros y usarlos para guardarlos en una receta.
                                   # Puede ser un metodo que ingrese de a uno o que pida todos los ingredientes. Cual sera mejor?
        """ Agrega los datos de un ingrediente en una receta"""
        return  # Desea ingresar otro ingrediente? sino finalizar metodo.
    
