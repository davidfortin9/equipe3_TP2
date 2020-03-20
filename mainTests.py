import whousedesign as wsd 
import whouse

whouse_inst = whouse.whouse(warehouse_width = 15,
warehouse_length = 20,)


print('*** Tests whousedesign ***')
print(str(wsd.wsd.add_arcs(whouse_inst)))
print(str(wsd.wsd.add_nodes(whouse_inst)))
print(str(wsd.wsd.add_slots(whouse_inst)))
print(str(wsd.wsd.draw_whouse(whouse_inst)))
