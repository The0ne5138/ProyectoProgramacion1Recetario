### **Ejercicio 2**

# Escribir una GUI que tenga una entrada de texto y un botón con la leyenda "Cambiar título". 
# El botón debe tomar lo que el usuario haya escrito en la entrada y colocarlo como título de la ventana. 
# Si no hay nada escrito en la entrada de texto debe mostrar una ventana emergente informando al usuario.  
  

# Marcar al botón como predeterminado, y hacer que también se accione cuando usuario presione la tecla Enter.  
  
import tkinter as tk
from tkinter import ttk, messagebox

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.window = parent
       
        self.entrada = tk.StringVar()
        ttk.Entry(self, width=60,
                  textvariable=self.entrada).grid(row=1, column=1,
                                                  padx=10, pady=10)
        boton = ttk.Button(self, text="Cambiar título",
                           default="active",
                           command=self.modificar_titulo)
        boton.grid(row=1, column=2, padx=10, pady=10)
        parent.bind("<Return>", lambda e: boton.invoke())
    
    def modificar_titulo(self):
        texto = self.entrada.get()
        if texto:
            self.window.title(texto)
        else:
            messagebox.showinfo(message="Debe escribir algo >.<")

root = tk.Tk()
App(root).grid()
root.mainloop()