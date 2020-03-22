
import math
from pyx import *
from tkinter import *
import whouse
import sqlite3

class wsd(whouse.whouse):

    def __init__(self, whouse):
        super(wsd, self).__init__()

    def add_arcs(self):
        #Connect to DB
        conn = sqlite3.connect('whouseDB.db')
        c = conn.cursor()

        #Get arcs from DB
        c.execute("SELECT * FROM arc")
        arcs_list = c.fetchall()
        arcs_dict = {}
        for i in arcs_list:
            val =[]
            key = i[0]
            val = list(i[1:])
            arcs_dict[key] = val
            arcs_dict.update()
            
        return arcs_dict
    
    def add_nodes(self):
        #Connect to DB
        conn = sqlite3.connect('whouseDB.db')
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

    def add_slots(self):
        #Connect to DB
        conn = sqlite3.connect('whouseDB.db')
        c = conn.cursor()

        #Get slots from DB
        c.execute("SELECT * from Slot")
        slots_list = c.fetchall()
        slots_dict = {}
        for i in slots_list:
            val = []
            key = i[0]
            val = list(i[1:])
            slots_dict[key] = val
            slots_dict.update()

        return slots_dict

   
    def draw_whouse(self):
        arcs = wsd.add_arcs(self)
        nodes = wsd.add_nodes(self)
        slots = wsd.add_slots(self)

        master = Tk()
        master.geometry('300x300')

        w = Canvas(master, height=self._warehouse_length*100, width =self._warehouse_width*100, bg="blue")

        # Lignes de contour
        w.create_rectangle(0, self._warehouse_length*10, self._warehouse_width*10, 0)


        # Lignes des arcs
        for arc_keys in arcs.keys():
            tail_node = arcs[arc_keys][1]
            head_node = arcs[arc_keys][2]
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
 





    # def twobyone(self):
    #     #Setting the depot node, and 2 main nodes above it
    #     depot_node = [1,"N0",0,0,0,"picker"]
    #     bottom_center_node = [2,"N1",depot_node[3],whouse.whouse.bottom_aisle_width()/2.0,0,"picker"]
    #     bottom_top_node = [3,"N2",depot_node[3],whouse.bottom_aisle_width(),0,"picker"]
        
    #     #Adding the nodes to the nodes list
    #     nodes = []
    #     nodes.append(depot_node)
    #     nodes.append(bottom_center_node)
    #     nodes.append(bottom_top_node)
        
    #     aisle_angle_pi = (float(whouse.aisle_angle_degree())/180)*math.pi
        
    #     slots = []
    #     #Arcs
    #     arcs = []
    #     # Creates the first to arc (from depot to the main node and from the bottom main node to top main node
    #     arc = [len(arcs)+1,1,depot_node[0],bottom_center_node[0]]
    #     arcs.append(arc)
    #     arc = [len(arcs)+1,1,bottom_center_node[0],bottom_top_node[0]]
    #     arcs.append(arc)
        
    #     #checks if the angle is 90 or 0
    #     if whouse.aisle_angle_degree()==0:
    #         angle_factor_x = 0
    #     if whouse.aisle_angle_degree() == 90:
    #         angle_factor_y = 0
    #     elif whouse.aisle_angle_degree()<90 and whouse.aisle_angle_degree()>0:
    #         angle_factor_y = 1/math.cos(aisle_angle_pi)
    #         angle_factor_x = 1/math.sin(aisle_angle_pi)

    #     #This case, the design is Chevron
    #     if whouse.aisle_angle_degree()<90 and whouse.aisle_angle_degree()>0:
    #         x_distance = whouse.node_distance()*angle_factor_x
    #         y_distance = whouse.node_distance()*angle_factor_y
    #         section_size = [(whouse.warehouse_length()-whouse.center_aisle_width())/2,whouse.warehouse_width()-whouse.bottom_aisle_width()]
    #         for i in range(1,int(section_size[0]/x_distance)+1):
    #             if i ==1:
    #             #if this the first node in the aisles, it will connect it to the main nodes
    #                 left_aisle_node = [len(nodes)+1,"N{}".format(len(nodes)),bottom_center_node[2]-(whouse.center_aisle_width()/2),bottom_center_node[3],0,"picker"]
    #                 arc = [len(arcs)+1,1,bottom_center_node[0],left_aisle_node[0]]
    #                 arcs.append(arc)
    #                 right_aisle_node = [len(nodes)+2,"N{}".format(len(nodes)),bottom_center_node[2]+(whouse.center_aisle_width()/2),bottom_center_node[3],0,"picker"]
    #                 arc = [len(arcs)+1,1,bottom_center_node[0],right_aisle_node[0]]
    #                 arcs.append(arc)
    #             elif i>1:
    #                 arc = [len(arcs)+1,1,left_aisle_node[0]]
    #                 left_aisle_node = [len(nodes)+1,"N{}".format(len(nodes)),left_aisle_node[2]-(x_distance),bottom_center_node[3],0,"picker"]
    #                 arc.append(left_aisle_node[0])
    #                 arcs.append(arc)
    #                 arc = [len(arcs)+1,1,right_aisle_node[0]]
    #                 right_aisle_node = [len(nodes)+2,"N{}".format(len(nodes)),right_aisle_node[2]+(x_distance),bottom_center_node[3],0,"picker"]
    #                 arc.append(right_aisle_node[0])
    #                 arcs.append(arc)
    #             nodes.append(left_aisle_node)
    #             nodes.append(right_aisle_node)
    #             aisle_node_l = [len(nodes)+1,"N{}".format(len(nodes)),left_aisle_node[2],left_aisle_node[3]+whouse.bottom_aisle_width()/2.0,0,"picker"]
    #             nodes.append(aisle_node_l)
    #             arc = [len(arcs)+1,1,left_aisle_node[0],aisle_node_l[0]]
    #             arcs.append(arc)
    #             aisle_node_r = [len(nodes)+1,"N{}".format(len(nodes)),right_aisle_node[2],right_aisle_node[3]+whouse.bottom_aisle_width()/2.0,0,"picker"]
    #             nodes.append(aisle_node_r)
    #             arc = [len(arcs)+1,1,right_aisle_node[0],aisle_node_r[0]]
    #             arcs.append(arc)
    #             for j in range(1,min(int((section_size[0]+(whouse.center_aisle_width()/2)-abs(aisle_node_r[2]))*angle_factor_y/(whouse.node_distance())),int((section_size[1]-abs(aisle_node_r[3]))*angle_factor_x/(whouse.node_distance())))):
    #                 y = aisle_node_r[3] + whouse.node_distance()*math.sin(aisle_angle_pi)*j
    #                 if j ==1:
    #                     arc_l = [len(arcs)+1,1,aisle_node_l[0]]
    #                     arc_r = [len(arcs)+2,1,aisle_node_r[0]]
    #                 elif j>1:
    #                     arc_l = [len(arcs)+1,1,node_l[0]]
    #                     arc_r = [len(arcs)+2,1,node_r[0]]
    #                 node_r = [len(nodes)+1,"N{}".format(len(nodes)),aisle_node_r[2]+(whouse.node_distance()*math.cos(aisle_angle_pi)*j),y,0,"picker"]
    #                 nodes.append(node_r)
    #                 node_l = [len(nodes)+1,"N{}".format(len(nodes)),aisle_node_l[2]-(whouse.node_distance()*math.cos(aisle_angle_pi)*j),y,0,"picker"]
    #                 nodes.append(node_l)
    #                 arc_l.append(node_l[0])
    #                 arc_r.append(node_r[0])
    #                 arcs.append(arc_l)
    #                 arcs.append(arc_r)
    #                 for i in range(whouse.slots_per_node()):
    #                     slot_r = []
    #                     slot_r.append(len(slots)+1)
    #                     slot_r.append(node_r[0])
    #                     slot_l = []
    #                     slot_l.append(len(slots)+2)
    #                     slot_l.append(node_l[0])
    #                     slots.append(slot_r)
    #                     slots.append(slot_l)
                        
    #         for i in range(1,int((whouse.warehouse_width()-whouse.bottom_aisle_width())/float(y_distance))):
    #             if i ==1:
    #                 arc = [len(arcs)+1,1,bottom_top_node[0]]
    #             elif i >1:
    #                 arc = [len(arcs)+1,1,aisle_node[0]]
    #             aisle_node = [len(nodes)+1,"N{}".format(len(nodes)),bottom_top_node[2],bottom_top_node[3]+y_distance*i,0,"picker"]
    #             nodes.append(aisle_node)
    #             arc.append(aisle_node[0])
    #             arcs.append(arc)
    #             aisle_node_r = [len(nodes)+1,"N{}".format(len(nodes)),bottom_top_node[2]+whouse.center_aisle_width()/2,bottom_top_node[3]+y_distance*i,0,"picker"]
    #             nodes.append(aisle_node_r)
    #             arc = [len(arcs)+1,1,aisle_node[0],aisle_node_r[0]]
    #             arcs.append(arc)
    #             aisle_node_l = [len(nodes)+1,"N{}".format(len(nodes)),bottom_top_node[2]-whouse.center_aisle_width()/2,bottom_top_node[3]+y_distance*i,0,"picker"]
    #             nodes.append(aisle_node_l)
    #             arc = [len(arcs)+1,1,aisle_node[0],aisle_node_l[0]]
    #             arcs.append(arc)
    #             for j in range(1,min(int((section_size[0]+(whouse.center_aisle_width()/2)-abs(aisle_node_r[2]))*angle_factor_y/(whouse.node_distance())),int((section_size[1]-abs(aisle_node_r[3]))*angle_factor_x/(whouse.node_distance())))):
    #                 y = aisle_node_r[3] + whouse.node_distance()*math.sin(aisle_angle_pi)*j
    #                 if j ==1:
    #                     arc_l = [len(arcs)+1,1,aisle_node_l[0]]
    #                     arc_r = [len(arcs)+2,1,aisle_node_r[0]]
    #                 elif j>1:
    #                     arc_l = [len(arcs)+1,1,node_l[0]]
    #                     arc_r = [len(arcs)+2,1,node_r[0]]
    #                 node_r = [len(nodes)+1,"N{}".format(len(nodes)),aisle_node_r[2]+(whouse.node_distance()*math.cos(aisle_angle_pi)*j),y,0,"picker"]
    #                 nodes.append(node_r)
    #                 node_l = [len(nodes)+1,"N{}".format(len(nodes)),aisle_node_l[2]-(whouse.node_distance()*math.cos(aisle_angle_pi)*j),y,0,"picker"]
    #                 nodes.append(node_l)
    #                 arc_l.append(node_l[0])
    #                 arc_r.append(node_r[0])
    #                 arcs.append(arc_l)
    #                 arcs.append(arc_r)
    #                 for i in range(whouse.slots_per_node()):
    #                     slot_r = []
    #                     slot_r.append(len(slots)+1)
    #                     slot_r.append(node_r[0])
    #                     slot_l = []
    #                     slot_l.append(len(slots)+2)
    #                     slot_l.append(node_l[0])
    #                     slots.append(slot_r)
    #                     slots.append(slot_l)

    #     return arcs, nodes, slots


    # #Doit afficher un widget de l'entrepôt
    # def draw_whouse(self, whouse):
    #     arcs, nodes, slots = self.twobyone(whouse)
    #     c = Canvas()
    #     for arc in arcs:
    #         c.create_line(arc[2], arc[3])
    #     # for node in nodes:
    #     #     c.create_oval(path.circle(node[3],node[4],1),[color.rgb.blue])
    #     c.create_image()
    #     print("Warehouse drawn")