import tkinter #as tk# tkinter (tk interface) es la interfaz por defecto de Python para el kit de herramientas de GUI (Graphical User Interface) Tk (ToolKit).
               # El paquete tkinter es una «interfaz Tk».
               # Tk como tkinter provienen de plataformas Unix. 
               # Tk en sí no es parte de Python, es mantenido por ActiveState.
               # tkinter es un conjunto de envoltorios que implementan los widgets(componentes) Tk como clases de Python.
               # Tcl (Tool Command Language) es un lenguaje de programación.
               # ActiveState es una Plataforma que permite el desarrollo y pruebas en ambientes Python y otros. 
               
rt = tkinter.Tk() # Creamos la raíz
rt.title("Bienvenidos!!!")     # Título de la ventana 
rt.iconbitmap('icono1.ico')  # Icono de la ventana, en ".ico" o ".xbm" en Linux
rt.geometry("600x400") # ancho x alto

#rt.state("zoomed") # maximizado

rt.resizable(0, 0)  # Desactivar redimensión de ventana  
rt.mainloop() # Creamos el bucle de la aplicación (estilo While True)