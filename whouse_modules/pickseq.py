#http://www.warehouselayout.org/sites/warehouselayout.org/files/pickseq.py.txt

import networkx as nx 
import whouse_modules.whousedesign as wsd 
import whouse_modules.whouse
import whouse_modules.graph

def sku_to_node_pick(sku_pick, slots, start_node_id):
	print("Creating a Node list from the SKU list...")
	node_pick = []
	node_pick.append(start_node_id)
	slot_pick = []
	for sku_id in sku_pick:
		for slot in slots:
			if len(slot)>2 and slot[2]==sku_id[2]:
				node_pick.append(slot[1])
				slot_pick.append(slot[0])
	return node_pick
	return slot_pick

def create_dist_matrix(node_pick, start_node_id, whouse_graph):
	dist_matrix=[]

	for node1 in sorted(node_pick):
		line=[]
		for node2 in sorted(node_pick):
			if node1 == start_node_id:
				line.append(nx.dijkstra_path_length(whouse_graph, start_node_id, node2))
			else:
				line.append(nx.dijkstra_path_length(whouse_graph, node1, node2))
		dist_matrix.append(line)
	
	return dist_matrix
	