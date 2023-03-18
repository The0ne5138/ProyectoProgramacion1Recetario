# Trabajo Práctico 2

#Las interfaces solicitadas en este Trabajo Práctico deben ser programadas aplicando POO.  
  

### **Ejercicio 1**

#Escribir una GUI con una ventana de un tamaño de 800x600 pixeles y que se posicione a 100 pixeles del borde izquierdo y 
# 100 pixeles del borde superior de la pantalla. 
# Como título, la ventana debe tener el texto, "Trabajo Práctico Nº2".  
  
#La ventana debe contener solo un botón con la leyenda "Terminar" y este debe terminar la ejecución del programa.    
  
import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.geometry("800x600+400+100")
        parent.title("Trabajo Práctico Nº2")
        
        ttk.Button(self, text="Terminar",
                   command=parent.destroy).grid(padx=10, pady=10)

root = tk.Tk()
App(root).grid()
root.mainloop()