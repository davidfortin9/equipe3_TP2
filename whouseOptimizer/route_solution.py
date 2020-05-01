import whouseOptimizer.solution as sol
import whouseOptimizer.fastroute_problem as frp 

import sys
import numpy as np

class Route(sol.Solution):

    def __init__(self, solvedProblem = frp.FastRouteProb(), 
                visit_sequence=list()):
        super(Route, self).__init__()
        self.visit_sequence = visit_sequence
        self.prob = solvedProblem
        self.proved_optimal = False

    def __str__(self):
        tmp_str = ', '.join([str(i) for i in self.visit_sequence])
        
        return str(tmp_str)
        
    def validate(self):
        location_list = list(range(0, self.prob.count_locations()))
        if sorted(self.visit_sequence) == location_list:
            return True

        # Vérifie que la capacité des pickers est respectée
        for seq in self.visit_sequence:
            load = 0
            for i in seq:
                if i != 1:
                    load = load + self.prob.d[i]

            if load <= self.prob.B:
                return True

        return False

    def evaluate(self):
        if self.validate() == False:
            # Pour nous, une solution non réalisable aura une très grande
            # valeur de fonction objectif.
            # (rappel: nous minimisons l'objectif)
            return sys.float_info.max
        obj_val = 0

        for seq in self.visit_sequence:
            for i in range(len(seq)-1):
                curr_source = seq[i]
                curr_destination = seq[i + 1]
                curr_distance = self.prob._dist_matrix[curr_source-1][curr_destination-1]
                
                print(curr_distance)
                obj_val = obj_val + curr_distance

        return obj_val
        