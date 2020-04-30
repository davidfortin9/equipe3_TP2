from whouse_modules.pickseq import sku_to_node_pick as sku_to_node_pick
from whouse_modules.pickseq import create_dist_matrix as create_dist_matrix
import whouse_modules.whouse as whouse

dist_matrix1 = [[0, 20, 30, 40], [20, 0, 30, 5], [30, 30, 0, 10], [40, 5, 10, 0]]

def short_dist_solver(sku_pick, whouse, node_pick, start_node_id):
    node_pick = sku_to_node_pick(sku_pick, whouse.slots, start_node_id)
    dist_matrix = create_dist_matrix(node_pick, start_node_id, whouse.whouse_graph)

    curr_node_id = node_pick.pop(0) # Parce que je suppose qu'on commence au premier objet dans la liste node_pick
    visit = [curr_node_id]
    while len(node_pick) - 1:

        min_dist = -1
        min_dist_node = -1
        for node in node_pick:
            if min_dist >= dist_matrix[curr_node_id][node] or min_dist_node == -1:
                min_dist  = dist_matrix[curr_node_id][node]
                min_dist_node = node
        curr_node_id = min_dist_node
        node_pick.remove(min_dist_node)
        visit.append(curr_node_id)
        print('curr_node_id = ')
        print(curr_node_id)
        print('node_pick = ')
        print(node_pick)
    visit.append(node_pick[-1])

    # Calcule la distance entre le start_node et tous les autres noeuds
    # Ajoute le noeud à la pickseq
    # Ajoute la distance à la obj value

    # Calculer la distance entre le noeud précédent et tous les autres noeuds
    # Ajoute le noeud à la pickseq
    # Ajoute la distance à la obj value
    # Répéter pour tous les noeuds



    

    # 




