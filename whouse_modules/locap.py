# http://www.warehouselayout.org/sites/warehouselayout.org/files/locap.py.txt

def coi(G, slots, line_item_sku, depot_node_id):
    from copy import copy
    import whouse_modules.graph
    import whouse_modules.whousedesign
    import networkx as nx
    sku_id_list = []

    # creating sku_id_list from slots
    for slot in slots:
        sku_id_list.append(slot[2])
    
    sku_index_list = []
    flat_line_item_sku_list = [item for sublist in line_item_sku for item in sublist]
    for id in sku_id_list:
        sku_index = [id, flat_line_item_sku_list.count(id)]
        sku_index_list.append(sku_index)
        # sorting the SKUs based on the popularity
        sku_index_list = sorted(sku_index_list, key=lambda sku_index_list: sku_index_list[1])
        sku_index_list.reverse()
        # Calculating the distance of each slot to the depot
    for slot in slots:
        distance_from_depot = nx.dijkstra_path_length(G,depot_node_id,slot[1])
        slot.append(distance_from_depot)
    #Sorting the Slots based on their closeness to the depot
    slots = sorted(slots, key=lambda slots: slots[4])
    #assigning the top SKUs to the TOP locations till one of them ends
    for i in range(min(len(sku_index_list),len(slots))):
        del slots[i][-1]
        slots[i].append(sku_index_list[i][0])
    print("Les emplacements les plus proches du noeud dépôt ont été assignés aux SKU les plus populaires")
    print("Format: ['slot_id[str], node_id[int], new_SKU[str], quantity[int], old_SKU[str]")
    return slots