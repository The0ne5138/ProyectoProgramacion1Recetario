# grid1.py
import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10, borderwidth=1, relief="groove")
        parent.title("Grid")
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=2)
        frame1 = ttk.Frame(self, borderwidth=2, relief="groove") # crea el frame
        frame1.grid(row=1, column=1, sticky=tk.NSEW) # inserta el frame a self
        frame1.columnconfigure(0, weight=1) # configura columna 0 (default)
        frame1.rowconfigure(0, weight=1) # configura fila 0 (default)
        ttk.Label(frame1, text="marco 1").grid(padx=5, pady=5) # crea, inserta label
        frame2 = ttk.Frame(self, borderwidth=1, relief="groove")
        frame2.grid(row=1, column=2, sticky=tk.NSEW)
        frame2.columnconfigure(0, weight=1)
        frame2.rowconfigure(0, weight=1)
        ttk.Label(frame2, text="marco 2").grid(padx=5, pady=5, sticky=tk.E)
        frame3 = ttk.Frame(self, borderwidth=1, relief="groove")
        frame3.grid(row=2, column=1, sticky=tk.NSEW)
        frame3.columnconfigure(0, weight=1)
        frame3.rowconfigure(0, weight=1)
        ttk.Label(frame3, text="marco 3").grid(padx=5, pady=5, sticky=tk.N)
        frame4 = ttk.Frame(self, borderwidth=1, relief="groove")
        frame4.grid(row=2, column=2, sticky=tk.NSEW)
        frame4.columnconfigure(0, weight=1)
        frame4.rowconfigure(0, weight=1)
        ttk.Label(frame4, text="marco 4").grid(padx=5, pady=5, sticky=tk.W)

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
App(root).grid(sticky=tk.NSEW)
root.mainloop()