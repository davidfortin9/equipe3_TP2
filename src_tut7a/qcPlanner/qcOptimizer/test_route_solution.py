import unittest
import sys

import qcPlanner.qcOptimizer.fastroute_problem as frp
import qcPlanner.qcOptimizer.route_solution as rsol

dist_matrix_small = [[0,  20,  30, 40],
                     [20,  0,  30,  5],
                     [30, 30,   0, 10],
                     [40,  5,  10,  0]]

class TestRoute(unittest.TestCase):
    def test_init(self):
        frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix_small)
        curr_rsol = rsol.Route(solvedProblem=frp_inst)

        # Initialement, la séquence doit être vide et la solution ne devrait 
        # pas être prouvée optimale au départ:
        self.assertTrue(curr_rsol.visit_sequence == [])
        self.assertFalse(curr_rsol.proved_optimal)

        # Dans un objet Route, on conserve une référence au problème.
        # Vérifions que c'est bien ce qui est fait.
        self.assertTrue(frp_inst is curr_rsol.problem)


    def test_validate(self):
        frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix_small)
        curr_rsol = rsol.Route(solvedProblem=frp_inst)

        # La séquence initiale devrait être invalide:
        self.assertFalse(curr_rsol.validate())

        # Ces séquences devraient être invalides:
        curr_rsol.visit_sequence = []
        self.assertFalse(curr_rsol.validate())
        curr_rsol.visit_sequence = [0, 2, 3]
        self.assertFalse(curr_rsol.validate())
        curr_rsol.visit_sequence = [1, 1, 1, 1]
        self.assertFalse(curr_rsol.validate())
        curr_rsol.visit_sequence = [1, 1, 1, 1, 1]
        self.assertFalse(curr_rsol.validate())

        # Ces séquences devraient être valides:
        curr_rsol.visit_sequence = [0, 1, 2, 3]
        self.assertTrue(curr_rsol.validate())
        curr_rsol.visit_sequence = [0, 2, 1, 3]
        self.assertTrue(curr_rsol.validate())


    def test_validate(self):
        frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix_small)
        curr_rsol = rsol.Route(solvedProblem=frp_inst)

        # La séquence initiale devrait devrait avoir une valeur de 
        # fonction objectif un grand float:
        self.assertAlmostEqual(curr_rsol.evaluate(), sys.float_info.max)

        # Ces séquences sont invalides, leur valeur de fonction objectif
        # devrait être un grand float:
        curr_rsol.visit_sequence = []
        self.assertAlmostEqual(curr_rsol.evaluate(), sys.float_info.max)
        curr_rsol.visit_sequence = [0, 2, 3]
        self.assertAlmostEqual(curr_rsol.evaluate(), sys.float_info.max)
        curr_rsol.visit_sequence = [1, 1, 1, 1]
        self.assertAlmostEqual(curr_rsol.evaluate(), sys.float_info.max)
        curr_rsol.visit_sequence = [1, 1, 1, 1, 1]
        self.assertAlmostEqual(curr_rsol.evaluate(), sys.float_info.max)

        # Pour les séquencs valide, la valeur de fonction objectif devrait
        # être correcte
        curr_rsol.visit_sequence = [0, 1, 2, 3]
        self.assertAlmostEqual(curr_rsol.evaluate(), 60)
        curr_rsol.visit_sequence = [0, 2, 1, 3]
        self.assertAlmostEqual(curr_rsol.evaluate(), 65)
