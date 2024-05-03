from tkinter import *

root = Tk()

etiqueta1 = Label(root, text="Noroeste").pack(anchor=NW)
etiqueta2 = Label(root, text="Norte").pack(anchor=N)
etiqueta3 = Label(root, text="Noreste").pack(anchor=NE)
etiqueta4 = Label(root, text="Oeste").pack(anchor=W)
etiqueta5 = Label(root, text="Centro").pack(anchor=CENTER)
etiqueta6 = Label(root, text="Este").pack(anchor=E)
etiqueta7 = Label(root, text="Suroeste").pack(anchor=SW)
etiqueta8 = Label(root, text="Sur").pack(anchor=S)
etiqueta9 = Label(root, text="Sureste").pack(anchor=SE)


root.mainloop()