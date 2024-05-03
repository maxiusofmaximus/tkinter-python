from tkinter import *

class Ventana:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Bandera Co")
        self.root.geometry("800x600")
        self.root.iconbitmap("tkinter_venv/python_code/img/Co.ico")
    
    def marco(self):
        marco = Frame()
        marco.pack()
        marco.config(width="800", height="600")
    
    def etiqueta(self):
        etiqueta = Label(self.root, text="Hola mundo")
        etiqueta.pack()
    
    def crear_ventana(self):
        self.root = Tk()
        etiqueta = Label(self.root, text="Hola mundo")
        etiqueta.pack()
        marco = Frame(self.root)
        marco.pack()
        marco.config(width="800", height="600")

def Secundaria(ventana1):
    ventana1.crear_ventana()

def Principal():
    ventana1 = Ventana(Tk())
    ventana1.etiqueta()
    ventana1.marco()
    pregunta = input("Te gustaría crear una nueva ventana?: ")
    if pregunta == "si":
        Secundaria(ventana1)
    ventana1.root.mainloop()

Principal()