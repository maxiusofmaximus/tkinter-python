from tkinter import *

root = Tk()

etiqueta = Label(root, text="Hola mundo")
etiqueta2 = Label(root, text="Chao mundo")

marco1 = Frame()
marco2 = Frame()

etiqueta.grid(row=0, column=0)
etiqueta2.grid(row=3, column=0)
marco1.grid(row=1, column=0)
marco2.grid(row=2, column=0)

marco1.config(width="400", height="200", bg="red")
marco2.config(width="400", height="200", bg="blue")


root.mainloop()