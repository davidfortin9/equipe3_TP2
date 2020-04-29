import unittest
import time
import sys

import qcPlanner.qcOptimizer.frp_rand_solver as frprs
import qcPlanner.qcOptimizer.fastroute_problem as frp
import qcPlanner.qcOptimizer.route_solution as rsol

dist_matrix_small = [[0,  20,  30, 40],
                     [20,  0,  30,  5],
                     [30, 30,   0, 10],
                     [40,  5,  10,  0]]

class TestFrpRandSolver(unittest.TestCase):
    def test_init(self):
        # Pas de tests pour l'instant
        pass

    def test_solve(self):
        # NOTE:
        # Le solveur étant aléatoire et implémantant une heuristique,
        # la solution retournée varie d'une exécution à l'autre.
        # Ceci complexifie les tests.
        frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix_small)
        frp_solver = frprs.FrpRandSolver()
        frp_solver.max_time_sec = 2
        frp_solver.verbose = 0
        start_time = time.time()
        frp_sol = frp_solver.solve(frp_inst)
        elapsed_time = time.time() - start_time

        # Si le solveur ne "triche" pas, l'exécution devrait durer au maximum
        # le temps attribué, j'ajoute une tolérance d'une seconde:
        self.assertLessEqual(elapsed_time, frp_solver.max_time_sec + 1.)
     

    def test_solve_correct(self):
        frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix_small)
        frp_solver = frprs.FrpRandSolver()
        frp_solver.max_time_sec = 2
        frp_solver.verbose = 0
        frp_sol = frp_solver.solve(frp_inst)

        # La solution retournée devrait avoir une valeur objectif 
        # non-négative:
        self.assertGreaterEqual(frp_sol.evaluate(), 0)

        # La solution retournée est-elle réalisable?
        self.assertTrue(frp_sol.validate())
