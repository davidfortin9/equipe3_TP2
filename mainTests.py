import whousedesign as wsd 
import whouse
import graph
import generator as gen 
from datetime import datetime
import orders
import pickseq

arcs = wsd.get_arcs()
nodes = wsd.get_nodes()
slots = wsd.get_slots()

print('*** Tests whousedesign ***')
print(str(arcs))
print(str(nodes))
print(str(slots))
print(str(wsd.draw_whouse(20,15)))


whouse_inst = whouse.whouse(warehouse_width=15,
                            warehouse_length=20,
                            arcs=arcs,
                            nodes=nodes,
                            slots=slots)

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


print("*** Test orders ***")
print(orders.get_orders())

print("*** Test pickseq ***")
sku_pick_inst = [[5, 'com1', 'SKU2'], [10, 'com1', 'SKU4'],[20, 'com2', 'SKU3'], [50, 'com2', 'SKU1']]
print(pickseq.sku_to_node_pick(sku_pick_inst, slots))