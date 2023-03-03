### **Ejercicio 4**
# Mejorar el ejercicio anterior revisando si la entrada de texto contiene algo antes de mostrar. 
# Si no contiene nada (la cadena vacía) mostrar una ventana emergente de información con el mensaje: 
# "Debe ingresar algo en la entrada de texto para poder mostrarlo."  
  
import tkinter as tk
from tkinter import ttk, messagebox

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.entrada = tk.StringVar()
        ttk.Entry(self, textvariable=self.entrada).grid(row=1, column=2)
        ttk.Button(self, text="Mostrar", command=self.mostrar).grid(row=1, column=3)

    def mostrar(self):
        contenido = self.entrada.get()
        if contenido == "":
            messagebox.showinfo(message=("Error! Entrada vacía."))
        else:
            print(contenido)

root = tk.Tk()
App(root).grid()
root.mainloop()
