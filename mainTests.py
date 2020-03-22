import whousedesign as wsd 
import whouse
import graph 

whouse_inst = whouse.whouse(warehouse_width = 15,
warehouse_length = 20,)


print('*** Tests whousedesign ***')
print(str(wsd.wsd.get_arcs(whouse_inst)))
print(str(wsd.wsd.get_nodes(whouse_inst)))
print(str(wsd.wsd.get_slots(whouse_inst)))
print(str(wsd.wsd.draw_whouse(whouse_inst)))

print("*** Tests graph ***")
graph.graph.nx_create(whouse_inst)
