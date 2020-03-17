#http://www.warehouselayout.org/sites/warehouselayout.org/files/pickseq.py.txt

import tlbx
import networkx as nx

'''
this module provides various algoriths for batching
typical parameters include:
	item_list (list) [quantity, order_id, sku_id]
	order_list (list) (id, order_dtg, target_pick_dtg , customer, order_number)
	batch_size (int)

outputs:
	sku_pickList (list[]) : a list of list of sku_ids to be picked in a single
'''
class pickseq(tlbx.tlbx):

	def __init__(self):
		super(pickseq, self).__init__()

	def order_in_one_all(self, *args):
		if len(args)==1:
			cnctn = args[0]
			print("Creating the batch of SKUs to be picked based on the each order in one trip logic...")
			sku_batch_list = []
			order_id_list = self.fetch_orders(cnctn,"id")
			line_item = self.fetch_line_item(cnctn)
			for order_id in order_id_list:
				sku_batch = []
				for line in line_item:
					if line[1] == order_id[0]:
						sku_batch.append(line[2])
				sku_batch_list.append(sku_batch)
			return sku_batch_list
		if len(args)==2:
			item_list = args[0]
			order_id_list = args[1]
			#single order pick list generator
			print("Creating the sequence of SKUs to be picked based on the each order in one trip logic...")
			sku_pick_list = []    
			for id in order_id_list:
				sku_pick = []
				for item in item_list:
					if id[0]==item[1]:
						sku_pick.append(item[2])
				sku_pick_list.append(sku_pick)
			return sku_pick_list		

	def fixed_batch_size_all (self, *args):
		if type(args[0])== list:
			item_list = args[0]
			batch_size = args[1]
			print("Creating the sequence of SKUs to be picked based on fixed number of SKUs per trip...")
			sku_pick_list = []    
			total_assigned = 0
			while total_assigned<len(item_list):
				if len(item_list)-total_assigned<batch_size:
					batch_size = len(item_list)-total_assigned
				for i in range(batch_size):
					sku_pick = []
					sku_pick.append(item_list[total_assigned][2])
					sku_pick_list.append(sku_pick)
				total_assigned = total_assigned +1
			return sku_pick_list
		else:
			cnctn = args[0]
			batch_size = args[1]
			print("Creating the sequence of SKUs to be picked based on fixed number of SKUs per trip...")
			connection = self.connection()
			cursor = connection.cursor()
			cursor.execute('select * from line_item')
			item_list = []
			for row in cursor:
				print(row)
				item_list.append(row)
			sku_pick_list = []
			total_assigned = 0
			while total_assigned<len(item_list):
				if len(item_list)-total_assigned<batch_size:
					batch_size = len(item_list)-total_assigned
				sku_pick = []
				for i in range(batch_size):
					sku_pick.append(item_list[total_assigned][2])
					total_assigned = total_assigned + 1
				sku_pick_list.append(sku_pick)
			for item in sku_pick_list:
				print(item)
			return sku_pick_list

	def sku_to_node_pick(self, *args):
		if type(args[0]) == list:
			sku_pick = args[0]
			slots = args[1]
			print("Creating a Node list from the SKU list...")
			node_pick = []
			slot_pick = []
			for sku_id in sku_pick:
				for slot in slots:
					if (len(slot)>2) and (slot[2]==sku_id):
						node_pick.append(slot[1])
						slot_pick.append(slot[0])
			return node_pick,slot_pick
		else:
			print("Creating a Node list from the SKU list...")
			sku_pick = args[0]
			connection = args[1]
			cursor = connection.cursor()
			cursor.execute('select * from slot')
			slots = []
			for row in cursor:
				slots.append(row)
			node_pick = []
			slot_pick = []
			for sku_id in sku_pick:
				query = 'select * from slot where sku_id = {}'.format(sku_id)
				cursor.execute(query)
				for row in cursor:
					node_pick.append(row[1])
					slot_pick.append(row[0])
			return node_pick,slot_pick