from .problem import Problem

import copy

class FastRouteProb(Problem):

    def __init__(self, name = "Fast route problem", dist_matrix=[[]]):
        super(FastRouteProb, self).__init__(name)
        self._dist_matrix = copy.deepcopy(dist_matrix)

    def __str__(self):
        tmp_str = self.name + '\n' + 'Distance matrix \n'
        for a_list in self._dist_matrix:
            tmp_str = tmp_str + '\t | '.join([str(i) for i in a_list])
            tmp_str = tmp_str + '\n'
        return str(tmp_str)

    def count_locations(self):
        return len(self._dist_matrix)
