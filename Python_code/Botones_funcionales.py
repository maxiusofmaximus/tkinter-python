from tkinter import *

root = Tk()

# Marco 1 de color amarillo
marco1 = Frame()
marco1.grid(row=0, column=0)
marco1.config(width="200", height="200", bg="yellow")

# Funcionalidad del boton 1 que al hacer click muestra una etiqueta de color verde
def f_boton1():
    etiqueta1 = Label(root, text="Botón presionado", padx=50, pady=90, bg="green")
    etiqueta1.grid(row=0, column=1)

# Boton 1 con funcionalidad en el marco rojo
boton1 = Button(root, text="Boton funcional", command=f_boton1).grid(row=0, column=0)

root.mainloop()