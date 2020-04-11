from tkinter import *
import sqlite3
import whousedesign as wsd
import graph
#from main import dist_matrix1
#from PIL import ImageTk, Image


root = Tk()
root.title('Olympus pick system')

'''Database'''

#conn = sqlite3.connect('')

#c = conn.cursor()

#conn.commit()

#conn.close()

'''Images'''

#seq_img = ImageTk.PhotoImage(whouse_graph)

'''Frames'''

frame = LabelFrame(root, padx=30, pady=25)
frame.pack(padx=10, pady=10)

frame1 = LabelFrame(root, text='Voici la tournée à effectuer', padx=1, pady=2)
frame1.pack(padx=20, pady=20)

'''Labels'''

label_e1 = Label(frame, text="Entrer la liste d'items à recueillir")
label_e1.grid(column=0, row=0)

label_e2 = Label(frame1, text='Item', padx=25)
label_e2.grid(column=0, row=3)

label_e3 = Label(frame1, text='Quantité', padx=25)
label_e3.grid(column=1, row=3)

label_e4 = Label(frame1, text='Localisation', padx=25)
label_e4.grid(column=2, row=3)

'''Entry'''

e1 = Entry(frame, width=60)
e1.insert(0, 'sku1, sku2, ...')
e1.grid(column=0, row=1)
#e.get()


'''Message box'''

#Ajouter les messages pour les retours vides (erreurs, pas de solution, etc)

'''Sliders'''

#Ajouter des sliders à root


'''Fonctions'''

def run():
    Lb1 = Listbox(frame1)
    Lb1.insert(1, 'Item 1')
    Lb1.insert(2, 'Item 2')
    Lb1.insert(3, 'Item 3')
    Lb1.insert(4, 'Item 4')
    Lb1.insert(5, 'Item 5')
    Lb1.grid(column=0, row=4)

    Lb2 = Listbox(frame1)
    Lb2.insert(1, '10')
    Lb2.insert(2, '10')
    Lb2.insert(3, '10')
    Lb2.insert(4, '10')
    Lb2.insert(5, '10')
    Lb2.grid(column=1, row=4)

    Lb3 = Listbox(frame1)
    Lb3.insert(1, 'A1')
    Lb3.insert(2, 'B1')
    Lb3.insert(3, 'C1')
    Lb3.insert(4, 'D1')
    Lb3.insert(5, 'E1')
    Lb3.grid(column=2, row=4)

    e1.delete(0, END)

    
'''def run1():
    res_label = Label(frame1, text=e1.get())
    res_label.grid(column=0, row=9)
    g = res_label.grid
    g = 0
    for l in res_label:
        g = l+1
        Listbox

    e1.delete(0, END)

    def clear_label(widget):
        widget['text'] = ''
    era_button = Button(frame1, text='Effacer', padx=30, command= lambda : clear_label(res_label))
    era_button.grid(column=1, row=10)    

    def graphik():
        arcs = wsd.get_arcs()
        nodes = wsd.get_nodes()
        slots = wsd.get_slots()
        print(arcs)
        whouse_graph = graph.nx_create(arcs, nodes)
        graph.nx_draw(arcs,nodes)

    graph_button = Button(frame1, text='Afficher le graphique', padx=10, command= lambda : graphik())
    graph_button.grid(column=1, row=11)'''



'''Bouttons'''

mybutton = Button(frame, text="Lancer", padx=30, command=run)
mybutton.grid(column=0,row=2)

button_quit = Button(root, text='Quitter', command=root.quit) #Il y a un bogue avec le boutton quand on lance le graph
button_quit.pack()




root.mainloop()
