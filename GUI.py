from tkinter import *
import sqlite3
from mainTests import sku_pick_inst



root = Tk()
root.title('Olympus pick system')

'''Database'''

#conn = sqlite3.connect('')

#c = conn.cursor()

#conn.commit()

#conn.close()

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

#label_e3 = Label(frame1, text='Résultats')
#label_e3.grid(column=1, row=2)

'''Entry'''

e1 = Entry(frame)
e1.grid(column=0, row=1)
e2 = Entry(frame)
e2.grid(column=0, row=4)


'''Message box'''

#Ajouter les messages pour les retours vides (erreurs, pas de solution, etc)

'''Fonctions'''

def run():
    order_list = Label(frame, text=e1.get())

def run2():
    label_e3 = Label(frame, text=e2.get())
    label_e3.grid(column=0, row=6)

def run3():
    res_label = Label(frame1, text=sku_pick_inst)
    res_label.grid(column=0, row=9)
    print(sku_pick_inst)    


'''Bouttons'''

mybutton = Button(frame, text="Lancer", padx=30, command=run)
mybutton.grid(column=0,row=2)

mybutton_e1 = Button(frame, text='Lancer', padx=30, command=run2)
mybutton_e1.grid(column=0, row=5)

button_quit = Button(root, text='Quitter', command=root.quit)
button_quit.pack()

res_button = Button(frame1, text='Obtenir les résultats', padx=30, command=run3)
res_button.grid(column=0, row=8)



root.mainloop()
