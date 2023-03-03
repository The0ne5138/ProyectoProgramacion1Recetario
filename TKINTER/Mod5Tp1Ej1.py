### **Ejercicio 1**
# Escribir una GUI con un botón con la leyenda "Mostrar fecha" y 
# que al presionarlo muestre por consola la fecha del día.

import tkinter as tk
from tkinter import ttk
import datetime

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Button(self, text="Mostrar fecha", command=self.mensaje).grid()

    def mensaje(self):
        print(datetime.datetime.now())

root = tk.Tk()
App(root).grid()
root.mainloop()