from tkinter import *

root = Tk()

# Etiqueta de texto
etiqueta1 = Label(root, text="Ingrese su nombre", padx=15, bg="white").grid(row=0, column=0)

# Entrada de datos del formulario
entrada1 = Entry(root)
entrada1.grid(row=0, column=1, padx=23)

# Insertar texto en la entrada
entrada1.insert(0, "Ingrese su nombre...")

# Funcionalidad del boton 1
def click_boton1():
    etiqueta = Label()
    etiqueta.grid(row=1, column=1)
    etiqueta.config(text=f'Se ha ingresado el nombre \n"{entrada1.get()}"', bg="green", padx=5)

# Boton 1
boton1 = Button(root, text="Enviar", bg="red", command=click_boton1, width=5, padx=10).grid(row=1, column=0)

root.mainloop()