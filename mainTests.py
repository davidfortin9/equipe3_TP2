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
import whouseOptimizer.route_solution as rsol 

print('*** Tests whousedesign ***')
arcs = wsd.get_arcs()
nodes = wsd.get_nodes()
slots = wsd.get_slots()
print("On devrait voir un dictionnaire contenant tous les arcs.  ('id': [travel_factor[float], head_node_id[int], tail_node_id[int])")
print(str(arcs))
print("On devrait voir un dictionnaire contenant tous les noeuds. (id[int]: name[str], x[float], y[float], z[float], type[str]) ")
print(str(nodes))
print("On devrait voir une liste contenant tous les emplacements de SKU. ([id[str], node_location_id[int], name[str], quantity[int]")
print(str(slots))
print("Une image de l'entrepôt devrait apparaître")
print(str(wsd.draw_whouse(20,15,arcs,nodes)))


whouse_inst = whouse.whouse(warehouse_width=15,
                            warehouse_length=20,
                             arcs=arcs,
                             nodes=nodes,
                             slots=slots)


print("*** Test graph ***")
whouse_graph = graph.nx_create(arcs, nodes)
print("Une image du graph de l'entrepôt devrait apparaître")
graph.nx_draw(arcs,nodes)

print("*** Tests generator ***")
print("Test order_datebound")
liste_commande = gen.order_datebound(3, datetime(2018,3,10), datetime(2018,4,10), 1)
print("Une liste  commandes est générée du 10 mars 2018 au 10 avril 2018 avec 3 commandes par jour")
print(liste_commande)
print("Test order_normal_datebound")
liste_commande_norm = gen.order_normal_datebound(3, 0.25, datetime(2018,3,10), datetime(2018,4,10),1)
print("Une liste de commandes est générée du 10 mars 2018 au 10 avril 2018 avec une moyenne de 3 commandes par jour et un écart type de 0.25 commandes par jour.")
print("Format d'une liste de commandes: orders = [[order1], [order2], [order3]...]")
print("Format d'une commande: order = [id[int], order_dtg[datetime], target_pick_dtg[datetime], customer[float], order_number[int]")
print(liste_commande_norm)
print("*** Test line_item_fixn ***")
print("Une liste de lignes de commandes est générée")
print("Format d'une ligne de commande: line_item = [quantity[int], order_id[float], SKU_id[float]]")
line_item_list = gen.line_item_fixn(slots, 3, 20, ['com1', 'com2', 'com3', 'com4'])
print(line_item_list)


print("*** Test pickseq ***")
print("Une liste de noeuds à visiter a été créer à partir de la liste de lignes de commandes générée ci-dessus.")
node_pick, slot_pick = pickseq.sku_to_node_pick(line_item_list, slots, 3)
print(node_pick)
print("Une liste d'emplacements à visiter a été créer à partir de la liste de lignes de commandes générée ci-dessus.")
print(slot_pick)
print("Une matrice des distances entre tous les noeuds contenu dans la liste de noeuds a été crée.")
dist_matrix = pickseq.create_dist_matrix(node_pick, 3 ,whouse_graph)
print(dist_matrix)

print('*** Test locap ***')
print(locap.coi(G=whouse_graph, slots=slots, line_item_sku=line_item_list, depot_node_id=1))


print('*** Test FrpProblems ***')
print('L\'instance devrait s\'afficher:')
frp_inst1 = frp.FastRouteProb(dist_matrix=dist_matrix,B=150,d={2:50,3:50,4:50,5:150},K=4, N=5)
print('c[i,j] = ' + str(frp_inst1._dist_matrix))
print('B = ' + str(frp_inst1.B))
print('d = ' + str(frp_inst1.d))
print('K = ' + str(frp_inst1.K))
print('N = ' + str(frp_inst1.N))


print("*** Test FrpAmplMipSolver *** ")
FrpAmplInst = FrpAmpl.FrpAmplMipSolver(prob=frp_inst1)
print(FrpAmpl.FrpAmplMipSolver.solve(FrpAmplInst))


# print('*** Test fastroute_problem ***')
# print(frp.FastRouteProb.count_locations(frp_inst1))

# print('**** Test route_solution ****')
# Route_inst1 = rsol.Route(solvedProblem=frp_inst1, visit_sequence=[[1,2,3,4,1], [1,5,1], [1,6,7,8,1]])
# Route_inst2 = rsol.Route(solvedProblem=frp_inst2, visit_sequence=[[1,2,3,4,1], [1,5,1], [1,6,7,8,1]])
# print('Test validate')
# print('Devrait être True')
# print(rsol.Route.validate(Route_inst1))
# print('Devrait être False')
# print(rsol.Route.validate(Route_inst2))
# print('Test evaluate')
# print(rsol.Route.evaluate(Route_inst1))

