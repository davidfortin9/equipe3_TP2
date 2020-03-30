#http://www.warehouselayout.org/sites/warehouselayout.org/files/pickseq.py.txt

import networkx as nx 
import whousedesign as wsd 
import whouse
import graph

def sku_to_node_pick(sku_pick, slots):
	sku_pick = sku_pick
	slots = slots
	print("Creating a Node list from the SKU list...")
	node_pick = []
	slot_pick = []
	for sku_id in sku_pick:
		for slot in slots:
			if (len(slot)>2) and (slot[2]==sku_id[2]):
				node_pick.append(slot[1])
				slot_pick.append(slot[0])
	return node_pick,slot_pick