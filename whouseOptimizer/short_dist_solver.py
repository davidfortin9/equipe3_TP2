from whouse_modules.pickseq import sku_to_node_pick as sku_to_node_pick
from whouse_modules.pickseq import create_dist_matrix as create_dist_matrix
import whouse_modules.whouse as whouse
import whouseOptimizer.solver as sl
from whouseOptimizer.fastroute_problem import FastRouteProb


class ShortDistance(sl.Solver):

    def __init__(self,prob):
        super(ShortDistance, self).__init__()
        self.prob = prob

    def solve(self):
        if type(self.prob) == FastRouteProb:
            dist_matrix = self.prob._dist_matrix
            n = len(dist_matrix)  + 1
            node_pick = list(range(1,n))
            print(node_pick)
            curr_node_id = node_pick.pop(0) # Parce que je suppose qu'on commence au premier objet dans la liste node_pick
            visit = [curr_node_id]
            while len(node_pick) - 1:

                min_dist = -1
                min_dist_node = -1
                for node in node_pick:
                    if min_dist >= dist_matrix[curr_node_id-1][node-1] or min_dist_node == -1:
                        min_dist  = dist_matrix[curr_node_id-1][node-1]
                        min_dist_node = node
                curr_node_id = min_dist_node
                node_pick.remove(min_dist_node)
                visit.append(curr_node_id)
            visit.append(node_pick[-1])
            visit.append(1)
            return visit






