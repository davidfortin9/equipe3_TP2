'''On va utiliser ce fichier comme point d'entrée pour le GUI. On va utiliser __main__ 
    pour l'interface en ligne de commande pour les tests en lots.'''

import whouse_modules.whousedesign as wsd 
import whouse_modules.whouse as whouse
import whouse_modules.graph as graph
import whouse_modules.generator as gen 
from datetime import datetime
import whouse_modules.orders as orders
import whouse_modules.pickseq as pickseq
import whouse_modules.locap as locap
import whouseOptimizer.FrpAmplMipSolver as FrpAmpl 
import whouseOptimizer.fastroute_problem as frp


arcs = wsd.get_arcs()
nodes = wsd.get_nodes()
slots = wsd.get_slots()
# print(arcs)
# print(nodes)

# print('*** Tests whousedesign ***')
# print(str(arcs))
# print(str(nodes))
# print(str(slots))
# print(str(wsd.draw_whouse(20,15,arcs,nodes)))


# # whouse_inst = whouse.whouse(warehouse_width=15,
# #                             warehouse_length=20,
# #                             arcs=arcs,
# #                             nodes=nodes,
# #                             slots=slots)


# print("*** Tests graph ***")
# whouse_graph = graph.nx_create(arcs, nodes)
# graph.nx_draw(arcs,nodes)


print("*** Tests generator")
# # print("Test order_datebound")
# # liste_commande = gen.order_datebound(3, datetime(2018,3,10), datetime(2018,4,10), 1)
# # print(liste_commande)
# # print(len(liste_commande))
# # print("Test order_normal_datebound")
# # liste_commande_norm = gen.order_normal_datebound(3, 0.25, datetime(2018,3,10), datetime(2018,4,10),1)
# # print(liste_commande_norm)
# # print(len(liste_commande_norm))
print("*** Test line_item_fixn ***")
print(gen.line_item_fixn(slots, 3, 20, ['com1', 'com2', 'com3', 'com4', 'com5']))
line_item_sku = [['com1', 'SKU1'], ['com2', 'SKU3'], ['com3', 'SKU3', 'SKU4'], ['com4', 'SKU2', 'SKU2'], ['com5', 'SKU3', 'SKU4', 'SKU4', 'SKU4']]


# print("*** Test pickseq ***")
# sku_pick_inst = [[5, 'com1', 'SKU2'], [10, 'com1', 'SKU4'],[20, 'com2', 'SKU3'], [50, 'com2', 'SKU1']]
# node_pick, slot_pick = pickseq.sku_to_node_pick(sku_pick_inst, slots, 3)
# print(node_pick)
# print(slot_pick)
# print(pickseq.create_dist_matrix(node_pick, 3 ,whouse_graph))



# print('*** Test locap ***')
# print(locap.coi(G=whouse_graph, slots=slots, line_item_sku=line_item_sku, depot_node_id=1))


print('*** Test FrpProblems ***')
print('L\'instance devrait s\'afficher:')
dist_matrix = [[0, 4.5, 6.5, 7.5, 10, 13, 10, 10],[8.5, 0, 1.9, 3, 2.7, 14, 12, 12],[13, 5, 0, 1.1, 3.5, 16, 13, 13],[12, 4.5, 4.5, 0, 2.4, 14, 12, 12],[13, 6.5, 5, 6, 0, 16, 13, 13],[8.5, 16, 15, 16, 19, 0, 2.6, 9],[6, 14, 13, 14, 16, 2.6, 0, 1],[5.5, 13, 12, 13, 15, 3.5, 8, 0]]
frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix)
print(str(frp_inst))

print("*** Test FrpAmplMipSolver *** ")
FrpAmplInst = FrpAmpl.FrpAmplMipSolver(prob=frp_inst,k=10,b=150,d={2:50,3:50,4:50,5:150,6:50,7:50,8:50}, N=8)
print(FrpAmpl.FrpAmplMipSolver.solve(FrpAmplInst)[0])
print(FrpAmpl.FrpAmplMipSolver.solve(FrpAmplInst)[1])


