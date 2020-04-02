from tkinter import *



root = Tk()
root.title('Olympus pick system')

'''Frames'''

frame = LabelFrame(root, padx=100, pady=25)
frame.pack(padx=20, pady=20)

frame1 = LabelFrame(root, text='Voici la tournée', padx=100, pady=50)
frame1.pack(padx=20, pady=20)

'''Labels'''

label_e1 = Label(frame, text="Entrer la liste d'items")
label_e1.grid(column=0, row=0)

label_e2 = Label(frame, text='Entrer le numéro de PO')
label_e2.grid(column=0, row=3)

label_e3 = Label(frame1, text='Affiche les résultats optimaux')
label_e3.grid(column=1, row=2)

'''Entry'''

e1 = Entry(frame)
e1.grid(column=0, row=1)
e2 = Entry(frame)
e2.grid(column=0, row=4)

'''Fonctions'''

def run():
    order_list = e1.get()

def allo():
    label_e3 = Label(frame, text=e2.get())
    label_e3.grid(column=0, row=6)

'''Bouttons'''

mybutton = Button(frame, text="Lancer", padx=30, command=run)
mybutton.grid(column=0,row=2)

mybutton_e1 = Button(frame, text='Lancer', padx=30, command=allo)
mybutton_e1.grid(column=0, row=5)

button_quit = Button(root, text='Quitter', command=root.quit)
button_quit.pack()



root.mainloop()
