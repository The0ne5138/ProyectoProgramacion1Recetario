# text.py
import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.cuadro_texto = tk.Text(self)
        self.cuadro_texto.grid(row=1, column=1, pady=10, padx=10, sticky=tk.NSEW)
        self.cuadro_texto.insert('1.0', "Este es el texto\ninicial del widget.")
        boton = ttk.Button(self, text="Mostrar", command=self.imprimir_texto)
        boton.grid(row=2, column=1, pady=5, padx=5)
        
    def imprimir_texto(self):
        texto = self.cuadro_texto.get('1.0', 'end')
        if texto != "": print(texto)
        
root = tk.Tk()
App(root).grid(row=1, column=1, sticky=tk.NSEW)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.mainloop()