# redimensionado.py
import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Prueba redimensionado").grid(pady=20, padx=20)
root = tk.Tk()

#root.resizable(tk.FALSE, tk.FALSE)
App(root).grid()
root.minsize(100, 100)
root.maxsize(500, 500)
root.attributes("-alpha", 0.7) #Entre 0.0 y 1.0
root.mainloop()