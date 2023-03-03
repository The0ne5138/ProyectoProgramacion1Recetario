
import tkinter

root = tkinter.Tk() # Creamos la raíz

frm = tkinter.Frame(root)
frm.grid()
tkinter.Label(frm, text="Bienvenidos a mi Sistema!").grid(column=0, row=0)
tkinter.Button(frm, text="Salir", command=root.destroy).grid(column=0, row=1)

root.mainloop() # Creamos el bucle de la aplicación (estilo While True)