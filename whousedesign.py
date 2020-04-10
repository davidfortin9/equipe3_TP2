
import math
from pyx import *
from tkinter import *
import whouse
import sqlite3

def get_arcs():
        #Connect to DB
        conn = sqlite3.connect('whouseDB.db')
        c = conn.cursor()

        #Get arcs from DB
        c.execute("SELECT * FROM Arc")
        arcs_list = c.fetchall()
        arcs_dict = {}
        for i in arcs_list:
            val =[]
            key = i[0]
            val = list(i[1:])
            arcs_dict[key] = val
            arcs_dict.update()
        
        return arcs_dict

def get_nodes():
        #Connect to DB
        conn = sqlite3.connect('whouse2DB.db')
        c = conn.cursor()

        #Get nodes from DB
        c.execute("SELECT * from Node")
        nodes_list = c.fetchall()
        nodes_dict = {}
        for i in nodes_list:
            val = []
            key = i[0]
            val = list(i[1:])
            nodes_dict[key] = val
            nodes_dict.update()

        return nodes_dict

def get_slots():
        #Connect to DB
        conn = sqlite3.connect('whouse2DB.db')
        c = conn.cursor()

        #Get slots from DB
        c.execute("SELECT * from Slot")
        slots_list_ini = c.fetchall()
        slots_list = []
        for i in slots_list_ini:
            e = list(i)
            slots_list.append(e)

        return slots_list

   
def draw_whouse(warehouse_length, warehouse_width, arcs, nodes):

        master = Tk()
        master.geometry('300x300')

        w = Canvas(master, height=warehouse_length*100, width =warehouse_width*100, bg="blue")

        # Lignes de contour
        w.create_rectangle(0, warehouse_length*10, warehouse_width*10, 0)


        # Lignes des arcs
        for arc_keys in arcs.keys():
            tail_node = int(arcs[arc_keys][1])
            head_node = int(arcs[arc_keys][2])
            x1 = nodes[tail_node][1]
            y1 = nodes[tail_node][2]
            x2 = nodes[head_node][1]
            y2 = nodes[head_node][2]
            w.create_line(x1*10, y1*10, x2*10, y2*10)

        #Points des nodes
        for node_key in nodes.keys():
            x1 = (nodes[node_key][1] - 0.5)*10
            y1 = (nodes[node_key][2] + 0.5)*10
            x2 = (nodes[node_key][1] + 0.5)*10
            y2 = (nodes[node_key][2] - 0.5)*10
            w.create_oval(x1, y1, x2, y2, fill = "red" )

        # Nom des nodes
        for node_name in nodes.keys():
            name = str(node_name)
            x = nodes[node_name][1]*10
            y = nodes[node_name][2]*10
            w.create_text(x, y, text = name, fill = "black")

        w.pack()
        master.mainloop()
 

    



