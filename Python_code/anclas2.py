from tkinter import *

root = Tk()
root.config(background="white")

etiqueta1 = Label(root, text="Hola mundo", bg="white", padx=10, pady=10).pack(anchor=NW)
etiqueta2 = Label(root, text="Contenido", bg="white", padx=10, pady=10).pack(anchor=NW)
etiqueta3 = Label(root, text="Chao mundo", bg="white", padx=10, pady=10).pack(anchor=NW)

root.mainloop()