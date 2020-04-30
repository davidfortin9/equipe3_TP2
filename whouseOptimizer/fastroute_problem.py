import whouseOptimizer.problem as prob
import whouse_modules.whouse as whouse

import copy



class FastRouteProb(prob.Problem):

    def __init__(self,  d=dict(), B=int(), N=int(), dist_matrix=[[]], K=int(), whouse=whouse.whouse()):
        super(FastRouteProb, self).__init__()
        self._dist_matrix = copy.deepcopy(dist_matrix)
        self.K = K
        self.B = B
        self.whouse = whouse
        self.d = d
        self.N = N

    def __str__(self):
        tmp_str = ''
        for a_list in self._dist_matrix:
            tmp_str = tmp_str + ', '.join([str(i) for i in a_list])
            tmp_str = tmp_str + '\n'
        return str(tmp_str)

    def count_locations(self):
        return len(self._dist_matrix)