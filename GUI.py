from tkinter import *

root = Tk()

label_e1 = Label(root, text="Entrer la liste d'items ici")
label_e1.grid(column=0, row=0)

e1 = Entry(root)
e1.grid(column=0, row=1)


def run():
    order_list = e1.get()



mybutton = Button(root, text="Run", command=run)
mybutton.grid(column=0,row=2)

root.mainloop()

