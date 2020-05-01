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
import whouseOptimizer.short_dist_solver as short_solver

print("Cette section effectue des tests en partant le la base de donnée whouseDB.db")
print('*** Tests whousedesign ***')
arcs = wsd.get_arcs('whouseDB.db')
nodes = wsd.get_nodes('whouseDB.db')
slots = wsd.get_slots('whouseDB.db')
print("On devrait voir un dictionnaire contenant tous les arcs.  ('id': [travel_factor[float], head_node_id[int], tail_node_id[int])")
print(str(arcs))
print("On devrait voir un dictionnaire contenant tous les noeuds. (id[int]: name[str], x[float], y[float], z[float], type[str]) ")
print(str(nodes))
print("On devrait voir une liste contenant tous les emplacements de SKU. ([id[str], node_location_id[int], name[str], quantity[int]")
print(str(slots))
print("Une image de l'entrepôt devrait apparaître")
print(str(wsd.draw_whouse(20,15,arcs,nodes)))

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
# On fixe la line_item_list pour obtenir la même sortie pour la méthode locap 
line_item_list = [[20, 'com1', 'SKU2'], [20, 'com1', 'SKU1'], [20, 'com1', 'SKU4'], [20, 'com2', 'SKU2'], [20, 'com2', 'SKU3'], [20, 'com2', 'SKU4'], [20, 'com3', 'SKU1'], [20, 'com3', 'SKU3'], [20, 'com3', 'SKU4'], [20, 'com4', 'SKU1'], [20, 'com4', 'SKU4'], [20, 'com4', 'SKU3']]


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
sol = FrpAmpl.FrpAmplMipSolver.solve(FrpAmplInst)
print(sol)
print("La visit_sequence est: " + str(sol[0])) #Modifier
print("La valeur de la fonction objective est: " + str(sol[1]))

print("Cette section fait des tests en partant de la base de donnée whouse2DB.db")

print('*** Tests whousedesign ***')
arcs = wsd.get_arcs('whouse2DB.db')
nodes = wsd.get_nodes('whouse2DB.db')
slots = wsd.get_slots('whouse2DB.db')
print("On devrait voir un dictionnaire contenant tous les arcs.  ('id': [travel_factor[float], head_node_id[int], tail_node_id[int])")
print(str(arcs))
print("On devrait voir un dictionnaire contenant tous les noeuds. (id[int]: name[str], x[float], y[float], z[float], type[str]) ")
print(str(nodes))
print("On devrait voir une liste contenant tous les emplacements de SKU. ([id[str], node_location_id[int], name[str], quantity[int]")
print(str(slots))
print("Une image de l'entrepôt devrait apparaître")
print(str(wsd.draw_whouse(20,15,arcs,nodes)))


whouse_inst = whouse.whouse(warehouse_width=30,
                            warehouse_length=50,
                             arcs=arcs,
                             nodes=nodes,
                             slots=slots)


print("*** Test graph ***")
whouse_graph = graph.nx_create(arcs, nodes)
print("Une image du graph de l'entrepôt devrait apparaître")
graph.nx_draw(arcs,nodes)

print("*** Tests generator ***")
print("Test order_datebound")
liste_commande = gen.order_datebound(5, datetime(2018,3,10), datetime(2018,6,10), 1)
print("Une liste  commandes est générée du 10 mars 2018 au 10 juin 2018 avec 5 commandes par jour")
print(liste_commande)
print("Test order_normal_datebound")
liste_commande_norm = gen.order_normal_datebound(10, 0.25, datetime(2018,3,10), datetime(2018,6,10),1)
print("Une liste de commandes est générée du 10 mars 2018 au 10 juin 2018 avec une moyenne de 3 commandes par jour et un écart type de 0.25 commandes par jour.")
print("Format d'une liste de commandes: orders = [[order1], [order2], [order3]...]")
print("Format d'une commande: order = [id[int], order_dtg[datetime], target_pick_dtg[datetime], customer[float], order_number[int]")
print(liste_commande_norm)
print("*** Test line_item_fixn ***")
print("Une liste de lignes de commandes est générée")
print("Format d'une ligne de commande: line_item = [quantity[int], order_id[float], SKU_id[float]]")
line_item_list = gen.line_item_fixn(slots, 3, 20, ['com1', 'com2', 'com3', 'com4'])
print(line_item_list)
# On fixe la line_item_list pour obtenir la même sortie pour la méthode locap 
line_item_list = [[20, 'com1', 'SKU38'], [20, 'com1', 'SKU18'], [20, 'com1', 'SKU4'], [20, 'com2', 'SKU20'], [20, 'com2', 'SKU35'], [20, 'com2', 'SKU47'], [20, 'com3', 'SKU23'], [20, 'com3', 'SKU35'], [20, 'com3', 'SKU31'], [20, 'com4', 'SKU30'], [20, 'com4', 'SKU21'], [20, 'com4', 'SKU12']]


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
frp_inst1 = frp.FastRouteProb(dist_matrix=dist_matrix,B=50,d={2:10,3:10,4:10,5:20,6:10,7:20,8:15,9:10,10:11,11:10,12:20},K=6, N=12)
print('c[i,j] = ' + str(frp_inst1._dist_matrix))
print('B = ' + str(frp_inst1.B))
print('d = ' + str(frp_inst1.d))
print('K = ' + str(frp_inst1.K))
print('N = ' + str(frp_inst1.N))

print("*** Test FrpAmplMipSolver *** ")
FrpAmplInst = FrpAmpl.FrpAmplMipSolver(prob=frp_inst1)
sol = FrpAmpl.FrpAmplMipSolver.solve(FrpAmplInst)
print(sol)
print("La visit_sequence est: " + str(sol[0]))
print("La valeur de la fonction objective est: " + str(sol[1]))

print("*** Test short_dist_solver ***")
short_dist_inst = short_solver.ShortDistance(prob=frp_inst1)
sol = short_solver.ShortDistance.solve(short_dist_inst)
print(sol)
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

