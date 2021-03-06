from tkinter import Tk, LabelFrame, Label, Text, Listbox, Button
from sqlite3 import connect
#import whousedesign as wsd
#import graph
#import mainTests as mt



root = Tk()
root.title('SIAD gestion d\'entrepôt')
root.geometry('500x525')


'''Frames'''

frame = LabelFrame(root, padx=30, pady=25)
frame.pack(padx=10, pady=10)

frame1 = LabelFrame(root, text='Voici la tournée à effectuer', padx=1, pady=2)
frame1.pack(padx=20, pady=20)

Lb1 = Listbox(frame1)
Lb2 = Listbox(frame1)
Lb3 = Listbox(frame1)
Lb1.grid(column=0, row=4)
Lb2.grid(column=1, row=4)
Lb3.grid(column=2, row=4)

'''Labels'''

label_e1 = Label(frame, text="Entrer la liste d'items à recueillir pour la commande")
label_e1.grid(column=0, row=0)

label_e2 = Label(frame1, text='Item', padx=25)
label_e2.grid(column=0, row=3)

label_e3 = Label(frame1, text='Quantité', padx=25)
label_e3.grid(column=1, row=3)

label_e4 = Label(frame1, text='Localisation', padx=25)
label_e4.grid(column=2, row=3)

'''Entry'''

TextArea = Text(frame, width=50, height=5)
TextArea.grid(column=0, row=1)

#e1 = Entry(frame, width=60)
#e1.insert(0, 'sku1, sku2, ...')
#e1.grid(column=0, row=1)



'''Message box'''

#Ajouter les messages pour les retours vides (erreurs, pas de solution, etc)

'''Sliders'''

#Ajouter des sliders à root


'''Fonctions'''

def run():

    pick_list = [[TextArea.get('1.0', '1.end'), '10', 'A1'], [TextArea.get('2.0', '2.end'), '15', 'A5'],
                [TextArea.get('3.0', '3.end'), '8', 'A2'], [TextArea.get('4.0', '4.end'), '14', 'B11'],
                 [TextArea.get('5.0', '5.end'), '7', 'B8']]

    #Envoie les entrées vers le problème du mainTests
    #send_list = [[TextArea.get('1.0', '1.end')],
    #            [TextArea.get('2.0', '1.end')],
    #            [TextArea.get('3.0', '1.end')],
    #            [TextArea.get('4.0', '1.end')],
    #            [TextArea.get('5.0', '1.end')]
    #            ]
                        
    
    #Retour de la solution du TSP dans les listbox
    #pick_list = [[mt.line_item_sku[1], mt.sku_pick_inst[1], mt.slot_pick[1]],
    #            [mt.line_item_sku[1], mt.sku_pick_inst[1], mt.slot_pick[1]],
    #            [mt.line_item_sku[1], mt.sku_pick_inst[1], mt.slot_pick[1]],
    #            [mt.line_item_sku[1], mt.sku_pick_inst[1], mt.slot_pick[1]],
    #            [mt.line_item_sku[2], mt.sku_pick_inst[2], mt.slot_pick[2]]
    #            ]

    Lb1 = Listbox(frame1)
    Lb2 = Listbox(frame1)
    Lb3 = Listbox(frame1)
    count = 1
    for pick in pick_list:
        #Lb1.insert(count, mt.sku_pick_inst[1:3])
        Lb1.insert(count, pick[0])
        Lb2.insert(count, pick[1])
        #Lb3.insert(count, mt.slot_pick[1])
        Lb3.insert(count, pick[2])
        count = count + 1

        Lb1.grid(column=0, row=4)
        Lb2.grid(column=1, row=4)
        Lb3.grid(column=2, row=4)

        #là on écrit directement la pick_list mais éventuellement quand le ampl va être terminé, va falloir utiliser
         #les différentes méthodes pour te fournir la pick_list et tu passe la pick_list dans la boucle
    

def erase_text():
    TextArea.delete(1.0, 'end')

#def erase_text2(widget):
 #   widget['text'] = ''    


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

era_button = Button(frame, text='Effacer', padx=30, command=erase_text)
era_button.grid(column=0, row=3)

button_quit = Button(root, text='Quitter', command=root.quit) 
button_quit.pack()




root.mainloop()
