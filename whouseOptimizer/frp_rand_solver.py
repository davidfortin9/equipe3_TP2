import whouseOptimizer.solver as sl 
import whouseOptimizer.fastroute_problem as frp 
import whouseOptimizer.route_solution as rsol

import numpy as np 
import time 
import copy


class FrpRandSolver(sl.Solver):

    def __init__(self, verbose=1):
        super(FrpRandSolver, self).__init__(verbose)

    def solve(self, prob=None):
        # Préparer exécution
        super(FrpRandSolver, self)._prepare()

        # Créer une première solution à partir du problème
        curr_rsol = rsol.Route(solvedProblem=prob)
        n_locations = curr_rsol.prob.count_locations()
        all_locations = range(0, n_locations)
        curr_rsol.visit_sequence = np.random.permutation(all_locations)
        if (self.verbose > 1):
            print('Solution initiale et objectif:')
            print(str(curr_rsol))
            print(str(curr_rsol.evaluate()))

            # Boucle d'exécution
            # Algorithme simple qui consiste à générer plusieurs solutions au hasard pour améliorer la solutio courante
        itération_no = 1
        while(self._continue()):
            if(self.verbose > 1):
                print('Itération ' + str(itération_no))
            new_rsol = rsol.Route(solvedProblem=prob)
            new_rsol.visit_sequence = np.random.permutation(all_locations)
            if (self.verbose > 1):
                print('Solution testée et objectif:')
                print(str(new_rsol))
                print(str(new_rsol.evaluate()))

            if new_rsol.evaluate() < curr_rsol.evaluate():
                curr_rsol = copy.deepcopy(new_rsol)
                if (self.verbose > 0):
                    print('Meilleure solution courante mise à jour:')
                    print(str(curr_rsol))
            itération_no = itération_no + 1

        # Finaliser l'exécution
        super(FrpRandSolver, self)._terminate()

        # Retourner une solution

        return curr_rsol