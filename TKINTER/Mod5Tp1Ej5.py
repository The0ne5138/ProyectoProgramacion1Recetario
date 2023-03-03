### **Ejercicio 5**
# Escribir una GUI con una etiqueta con el texto: "Ingrese un número", 
# seguido de una entrada de texto y finalmente un botón con la leyenda: 
# "Calcular la raíz cuadrada".  
# Al hacer click en el botón, se debe ejecutar el cálculo de la raíz cuadrada 
# del número ingresado en el "Entry" y mostrarlo por consola.  
  
import tkinter as tk
from tkinter import ttk, messagebox
import math

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.entrada = tk.StringVar()
        ttk.Label(self, text="Ingrese un número", padding=3).grid(row=1, column=1)
        ttk.Entry(self, textvariable=self.entrada).grid(row=1, column=2)
        ttk.Button(self, text="Calcular raíz cuadrada", command=self.mostrar).grid(row=1, column=3)

    def mostrar(self):
        contenido = self.entrada.get()
        if contenido == "":
            messagebox.showinfo(message=("Error! Debe ingresar un número para poder realizar el cálculo!"))
        else:
            numero = int(contenido)
            print(math.sqrt(numero))

root = tk.Tk()
App(root).grid()
root.mainloop()
