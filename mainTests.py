import whousedesign as wsd 
import whouse
import graph
import generator as gen 
from datetime import datetime

whouse_inst = whouse.whouse(warehouse_width = 15,
warehouse_length = 20,)


print('*** Tests whousedesign ***')
print(str(wsd.wsd.get_arcs(whouse_inst)))
print(str(wsd.wsd.get_nodes(whouse_inst)))
print(str(wsd.wsd.get_slots(whouse_inst)))
print(str(wsd.wsd.draw_whouse(whouse_inst)))

print("*** Tests graph ***")
graph.graph.nx_draw(whouse_inst)

print("*** Tests generator")
print("Test sku")
print(gen.sku(20))
print("Test order_datebound")
liste_commande = gen.order_datebound(3, datetime(2018,3,10), datetime(2018,4,10), 1)
print(liste_commande)
print(len(liste_commande))
print("Test order_normal_datebound")
liste_commande_norm = gen.order_normal_datebound(3, 0.25, datetime(2018,3,10), datetime(2018,4,10),1)
print(liste_commande_norm)
print(len(liste_commande_norm))