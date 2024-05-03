from tkinter import *
from tkinter.messagebox import *

root = Tk()

def mensaje():
    showinfo(title="Aquí se muestra el título de la ventana.", message="Aquí se muestra la información dentro del cuadro de diálogo.")
    showwarning(title="Aquí se muestra el titulo de advertencia", message="Aquí se muestra el mensaje de advertencia")
    showerror(title="Aquí se muestra el titulo de error", message="Aquí se muestra el mensaje de error")

def mensaje2():
    askquestion(title="Aquí se muestra el título de la ventana de pregunta", message="Aquí se muestra el mensaje de pregunta")
    askyesno(title="Aquí se muestra el título de la ventana de yes / no", message="Aquí se muestra el mensaje de yes / no")
    askyesnocancel(title="Aquí se muestra el título de la ventana de re-pregunta", message="Aquí se muestra el mensaje de re-pregunta")
    askokcancel(title="Aquí se muestra el título de la ventana de cancelar", message="Aquí se muestra el mensaje de cancelar")
    askretrycancel(title="Aquí se muestra el título de la ventana de re-cancelar", message="Aquí se muestra el mensaje de re-cancelar")

boton1 = Button(root, text="Get mensaje", command=mensaje).pack(anchor=CENTER)
boton1 = Button(root, text="Get pregunta", command=mensaje2).pack(anchor=CENTER)

root.mainloop()