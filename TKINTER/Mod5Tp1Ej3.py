### **Ejercicio 3**
# Escribir una GUI con una entrada de texto y un botón con la leyenda "Mostrar". 
# Al hacer click en el botón se debe mostrar el contenido de la entrada de texto por consola.  
  
import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.entrada = tk.StringVar()
        ttk.Entry(self, textvariable=self.entrada).grid(row=1, column=2)
        ttk.Button(self, text="Mostrar",command=self.mostrar).grid(row=1, column=3)

    def mostrar(self):
        print(self.entrada.get())

root = tk.Tk()
App(root).grid()
root.mainloop()
