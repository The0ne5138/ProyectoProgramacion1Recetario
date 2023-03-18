# boton_cierre.py

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.ventana = parent
        ttk.Label(self, text="Prueba WM_DELETE_WINDOW").grid(padx=5, pady=5)
        parent.protocol("WM_DELETE_WINDOW", self.on_cerrar)

    def on_cerrar(self):
        res = askyesno(title="Confirmar",message="¿Desea guardar los cambios antes de salir")
        if res:
            print("Se guardaron los cambios.")
        else:
            print("No se guardaron los cambios.")
        self.ventana.destroy()

root = tk.Tk()
#root.resizable(tk.FALSE, tk.FALSE)
App(root).grid()
root.mainloop()