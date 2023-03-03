### **Ejercicio 2**
# Escribir una GUI con dos botones, uno con la leyenda "Info" y 
# otro con la leyenda "Advertencia". Al hacer click a uno, 
# debe mostrar una ventana emergente **de información** con el mensaje que Ud. quiera. 
# Y el otro debe mostrar una ventana emergente **de advertencia**, también, con el mensaje que Ud. quiera.  
  
import tkinter as tk
from tkinter import ttk, messagebox

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Button(self, text="Info", command=self.mensaje_info).grid()
        ttk.Button(self, text="Advertencia", command=self.mensaje_advertencia).grid()

    @staticmethod
    def mensaje_info():
        messagebox.showinfo(message="Le informo que Ud. presionó un botón.")

    @staticmethod
    def mensaje_advertencia():
        messagebox.showwarning(message=("Ojo con este botón. Queda Ud."
                                        " debidamente advertido."))

root = tk.Tk()
App(root).grid()
root.mainloop()