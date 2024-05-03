from tkinter import *

root = Tk()

# Guarda la opción elegida
guardar_opcion = IntVar()

# Se le da un valor predefinido en guardar opción
guardar_opcion.set(value=1)

# Aquí se puede ver la opción que escoge el usuario
def imprimir_opcion():
    print(guardar_opcion.get())

# Se ingresa una etiqueta para dar indicaciones
titulo = Label(root, text="Seleccione la respuesta correcta").grid(row=0, padx=10, pady=10)

# Se ingresa una etiqueta que hace una pregunta
texto = Label(root, text="¿Cuál es el diámetro de la Vía Láctea?").grid(row=1, padx=10, pady=10)

# Se crean las opciones para escoger una respuesta
lista_opciones = [Radiobutton(root, text="Cien mil años luz", value=1, variable=guardar_opcion,             command=imprimir_opcion),
                  Radiobutton(root, text="Cincuenta mil años luz", value=2, variable=guardar_opcion, command=imprimir_opcion),
                  Radiobutton(root, text="Vienta mil kilómetros", value=3, variable=guardar_opcion, command=imprimir_opcion),
                  Radiobutton(root, text="Vienta mil años luz", value=4, variable=guardar_opcion, command=imprimir_opcion)]

# Se iteran las opciones para mostrarlas en la ventana root
for op in range(0, 4):
    lista_opciones[op].grid(row=2+op, padx=10, pady=10)

# Este botón envía las respuestas
b_enviar = Button(root, text="Enviar respuesta", bg="green").grid(row=6, padx=10, pady=10)

root.mainloop()