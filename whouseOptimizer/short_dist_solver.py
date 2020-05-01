from whouse_modules.pickseq import sku_to_node_pick as sku_to_node_pick
from whouse_modules.pickseq import create_dist_matrix as create_dist_matrix
import whouse_modules.whouse as whouse
import whouseOptimizer.solver as sl

class ShortDistance(sl.Solver):

    def __init__(self):
        super(ShortDistance).__init__()

    def short_dist_solver(self, frp_inst):
        node_pick = sku_to_node_pick(frp_inst.sku_pick, frp_inst.whouse.slots, frp_inst.start_node_id)
        dist_matrix = frp_inst._dist_matrix

        curr_node_id = node_pick[0].pop(0) # Parce que je suppose qu'on commence au premier objet dans la liste node_pick
        visit = [curr_node_id]
        while len(node_pick) - 1:

            min_dist = -1
            min_dist_node = -1
            for node in node_pick:
                if min_dist >= dist_matrix[curr_node_id][node] or min_dist_node == -1:
                    min_dist  = dist_matrix[curr_node_id][node]
                    min_dist_node = node
            curr_node_id = min_dist_node
            node_pick[0].remove(min_dist_node)
            visit.append(curr_node_id)
            print('curr_node_id = ')
            print(curr_node_id)
            print('node_pick = ')
            print(node_pick)
        visit.append(node_pick[-1])
        return visit

        # Calcule la distance entre le start_node et tous les autres noeuds
        # Ajoute le noeud à la pickseq
        # Ajoute la distance à la obj value

        # Calculer la distance entre le noeud précédent et tous les autres noeuds
        # Ajoute le noeud à la pickseq
        # Ajoute la distance à la obj value
        # Répéter pour tous les noeuds



    

        # 




