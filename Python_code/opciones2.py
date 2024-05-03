from tkinter import *

root = Tk()

def actualiza():
    opcion_set = Label(root, text=colores.get()).grid(row=6)

titulo = Label(root, text="Seleccione una opcion.").grid(row=0)

opciones = ["rojo", "azul", "verde", "amarillo"]

colores = StringVar()
colores.set(value=opciones[0])

for valor in range(0, len(opciones)):
    Radiobutton(root, text=f"Color {opciones[valor]}", variable=colores, value=opciones[valor], padx=10, pady=10).grid(row=1+valor)

enviar = Button(root, text="Enviar formulario", command=actualiza, bg="green", padx=10, pady=10).grid(row=5)

root.mainloop()