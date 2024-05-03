from tkinter import *

root = Tk()

# Marco 1 de color rojo
marco1 = Frame()
marco1.grid(row=0, column=0)
marco1.config(width="200", height="200", bg="red")

# Marco 2 de color rojo
marco2 = Frame()
marco2.grid(row=0, column=1)
marco2.config(width="200", height="200", bg="yellow")

# Marco 3 de color rojo
marco3 = Frame()
marco3.grid(row=1, column=0)
marco3.config(width="200", height="200", bg="blue")

# Marco 4 de color rojo
marco4 = Frame()
marco4.grid(row=1, column=1)
marco4.config(width="200", height="200", bg="orange")

# Marco 5 de color rojo
marco5 = Frame()
marco5.grid(row=2, column=0)
marco5.config(width="200", height="200", bg="purple")

# Marco 6 de color rojo
marco6 = Frame()
marco6.grid(row=2, column=1)
marco6.config(width="200", height="200", bg="pink")

# Boton 1 de color amarillo de 75 píxeles de alto sin funcionalidad en el marco rojo
boton1 = Button(root, text="No toques el botón", bg="yellow", pady=75).grid(row=0, column=0)

# Boton 2 de color naranja de 75 píxeles de alto sin funcionalidad en el marco azul
boton2 = Button(root, text="No toques el botón", bg="orange", pady=75, state=DISABLED).grid(row=1, column=0)

# Etiqueta 1 de color rojo de 50 píxeles de ancho en el marco amarillo
etiqueta1 = Label(root, text="Etiqueta de texto", bg="red", padx=50).grid(row=0, column=1)

root.mainloop()