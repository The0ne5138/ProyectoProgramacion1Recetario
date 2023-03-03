### **Ejercicio 6**
# Mejorar el ejercicio anterior revisando si la entrada de texto contiene algo
# y si el texto que contiene puede castearse a 'int'.  
# Si no contiene nada, mostrar una ventana emergente informándolo.  
# Si contiene algo, pero no se puede castear a 'int'. 
# mostrar una ventana emergente de error, informando que sólo se espera que se ingresen números enteros.  
# Aplicar manejo de errores para resolver el casteo a 'int'.
  
import tkinter as tk
from tkinter import ttk, messagebox
import math

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.entrada = tk.StringVar()
        ttk.Label(self, text="Ingrese un número", padding=3).grid(row=1, column=1)
        ttk.Entry(self, textvariable=self.entrada).grid(row=1, column=2)
        ttk.Button(self, text="Calcular raiz cuadrada",
                   command=self.mostrar).grid(row=1, column=3)

    def mostrar(self):
        contenido = self.entrada.get()
        if contenido == "":
            messagebox.showinfo(message=("Error! Entrada vacía."))
        else:
            try:
                numero = int(contenido)
            except ValueError:
                messagebox.showerror(message="Error! Debe ingresar un número real.")
            else:
                if numero > 0:
                    print(math.sqrt(numero))
                else:
                    messagebox.showerror(message="Error! Debe ingresar un número positivo.")

root = tk.Tk()
App(root).grid()
root.mainloop()