import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        # definimos las columnas
        columns = ('nombre', 'apellido', 'email')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.grid(row=1, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        # definimos los encabezados
        self.tree.heading('nombre', text='Nombre')
        self.tree.heading('apellido', text='Apellido')
        self.tree.heading('email', text='e-mail')
        # generar los datos artificiales
        contacts = []
        for n in range(1, 30):
            contacts.append((f'Nombre {n}', f'Apellido {n}', f'email{n}@example.com'))
        # agregar datos al treeview
        for contact in contacts:
            self.tree.insert('', tk.END, values=contact)
        # para ejecutar un callback cuando se haga click en un item
        self.tree.bind('<<TreeviewSelect>>', self.item_seleccionado)
        # agregar barra de scroll
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky=(tk.N, tk.S))
        
    def item_seleccionado(self, event):
        for seleccionado in self.tree.selection():
            item = self.tree.item(seleccionado)
            fila = item['values']
            # mostrar mensaje
            showinfo(title='Informacion', message=','.join(fila))

root = tk.Tk()
App(root).grid()
root.title('Ejemplo de Treeview')
root.mainloop()
