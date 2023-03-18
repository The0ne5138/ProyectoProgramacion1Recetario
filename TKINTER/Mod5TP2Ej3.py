### **Ejercicio 3**

import tkinter as tk
from tkinter import ttk, messagebox

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.window = parent
        self.window.title("Ejercicio 3")
        self.window.geometry("400x200+400+200")
        self.sesion = False
    
        self.etiqueta = ttk.Label(text="").grid(row=1, column=1, padx=3, pady=3)
        self.boton = ttk.Button(self, text="Iniciar sesión",
                                default="active",
                                command=self.login)
        self.boton.grid(row=1, column=2, padx=10, pady=10)
    
    def login(self):
        if self.sesion:
            self.logout()
        else:
            ventana_login = tk.Toplevel(self.window)
            Login(ventana_login, self).grid()
    
    def login_correcto(self):
        self.boton["text"] = "Cerrar sesión"
        self.sesion = True
    
    def logout(self):
        self.boton["text"] = "Iniciar sesión"
        self.sesion = False

class Login(ttk.Frame):
    def __init__(self, parent, main_window):
        super().__init__(parent, padding=10)
        self.main_window = main_window
        self.window = parent
        self.window.title("Iniciar sesión")
        self.usuario = tk.StringVar()
        self.passw = tk.StringVar()
        
        ttk.Label(self, text="Nombre de usuario", padding=3).grid(row=1, column=1)
        ttk.Entry(self, textvariable=self.usuario).grid(row=1, column=2)
        ttk.Label(self, text="Contraseña", padding=3).grid(row=2, column=1)
        ttk.Entry(self, textvariable=self.passw, show="*").grid(row=2, column=2)
        btn_guardar = ttk.Button(self, text="Iniciar", command=self.iniciar_sesion)
        btn_cancelar = ttk.Button(self, text="Cancelar", command=self.window.destroy)
        btn_cancelar.grid(row=10, column=2)
        btn_guardar.grid(row=10, column=3)
    
    def iniciar_sesion(self):
        if True:
            self.main_window.login_correcto()
        self.window.destroy()

root = tk.Tk()
App(root).grid()
root.mainloop()