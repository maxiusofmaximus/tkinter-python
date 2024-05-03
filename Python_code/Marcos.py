from tkinter import *

root = Tk()
root.title("Bandera Co")
root.iconbitmap("tkinter_venv/python_code/img/Co.ico")

marco_principal = Frame()
marco_principal2 = Frame()
marco_principal3 = Frame()

marco_principal.pack()
marco_principal2.pack()
marco_principal3.pack()

marco_principal.config(width="400", height="300", bg="yellow")
marco_principal2.config(width="400", height="200", bg="blue")
marco_principal3.config(width="400", height="200", bg="red")

root.mainloop()