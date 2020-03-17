
#http://www.warehouselayout.org/sites/warehouselayout.org/files/locap.py.txt
import tlbx

class locap(tlbx.tlbx):

    def __init__(self):
        super(locap, self).__init__()

    def random(self, *args):
        if len(args)==1:
            cnctn = args[0]
            slot_list = self.fetch_slot(cnctn)
            sku_id_list = self.fetch_sku(cnctn,'id')
            return self.random(slot_list, sku_id_list)
        if len(args)==2:
            slot_list = args[0]
            sku_id_list = args[1]
            from random import sample
            sku_id_list_random = sample(sku_id_list,len(sku_id_list))
            for i in range(min(len(slot_list),len(sku_id_list_random))):
                slot_quantity = 5
                slot_sku_id = sku_id_list_random[i]
                slot = []
                slot_list[i].append(slot_sku_id)
                slot_list[i].append(slot_quantity)
            return slot_list

    def coi(self, *args):
        if len(args)==3:
            graph = args[0]
            cnctn = args[1]
            depot_node_id = args[2]        
            line_item_sku = self.fetch_line_item(cnctn,'sku_id')
            slots = self.fetch_slot(cnctn)
            sku_id_list = self.fetch_sku(cnctn,'id')
            return self.coi(graph, line_item_sku, slots, sku_id_list, depot_node_id)
        if len(args)==5:
            graph = args[0]
            line_item_sku = args[1]
            slots = args[2]
            sku_id_list = args[3]
            depot_node_id = args[4]
            from copy import copy
            import graph
            sku_index_list = []
            for id in sku_id_list:
                sku_index = [id, line_item_sku.count(id)]
                sku_index_list.append(sku_index)
                # sorting the SKUs based on the popularity
                sku_index_list = sorted(sku_index_list, key=lambda sku_index_list: sku_index_list[2])
                # Calculating the distance of each slot to the depot
            for slot in slots:
                pick_seq = [0,slot[0]]
                distance_matrix = graph.nx_dijkstra_dm(graph,pick_seq)
                slot.append(distance_matrix[0][1])
            #Sorting the Slots based on their closeness to the depot
            slots = sorted(sku_index_list, key=lambda slots: slots[2], reverse=True)
            #assigning the top SKUs to the TOP locations till one of them ends
            for i in range(min(len(sku_index_list),len(slots))):
                del slots[i][-1]
                slots[i].append(sku_index_list[i][0])
            return slots
            