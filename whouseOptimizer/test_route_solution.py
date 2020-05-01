import unittest
import sys
import whouse_modules.whouse as whouse
import whouse_modules.whousedesign as wsd

import whouseOptimizer.fastroute_problem as frp
import whouseOptimizer.route_solution as rsol

arcs = wsd.get_arcs('whouseDB.db')
nodes = wsd.get_nodes('whouseDB.db')
slots = wsd.get_slots('whouseDB.db')

whouse_inst = whouse.whouse(warehouse_width=15,
                             warehouse_length=20,
                              arcs=arcs,
                              nodes=nodes,
                              slots=slots)

c = [[0, 7, 11, 15, 19],
    [7, 0, 18, 22, 26],
    [11, 18, 0, 18, 22],
    [15, 22, 18, 0, 18],
    [19, 26, 22, 18, 0]]

B = 150
d = {2: 50, 3: 50, 4: 50, 5: 150}
K = 4
N = 5

visit_sequence = [[1.0, 2.0, 1.0], [1.0, 3.0, 4.0, 1.0], [1.0, 5.0, 1.0]]

class TestRoute(unittest.TestCase):
    def test_init(self):
        frp_inst = frp.FastRouteProb(d=d, B=B, N=N, dist_matrix=c, K=K, whouse=whouse_inst)
        curr_rsol = rsol.Route(solvedProblem=frp_inst, visit_sequence=[[1.0, 2.0, 1.0], [1.0, 3.0, 4.0, 1.0], [1.0, 5.0, 1.0]])

        # Dans un objet Route, on conserve une référence au problème.
        # Vérifions que c'est bien ce qui est fait.
        self.assertTrue(frp_inst is curr_rsol.prob)


    def test_validate(self):
        frp_inst = frp.FastRouteProb(d=d, B=B, N=N, dist_matrix=c, K=K, whouse=None)
        curr_rsol = rsol.Route(solvedProblem=frp_inst, visit_sequence=[[1.0, 2.0, 1.0], [1.0, 3.0, 4.0, 1.0], [1.0, 5.0, 1.0]])


        # La séquence initiale devrait être invalide:
        self.assertFalse(curr_rsol.validate())

        # Ces séquences devraient être invalides:
        curr_rsol.visit_sequence = []
        self.assertFalse(curr_rsol.validate())
        curr_rsol.visit_sequence = [[1.0, 2.0, 1.0], [2.0, 3.0, 4.0, 1.0], [6.0, 5.0, 1.0]]
        self.assertFalse(curr_rsol.validate())
        curr_rsol.visit_sequence = [[1.0, 1.0, 1.0], [1.0, 1.0, 4.0, 1.0], [1.0, 1.0, 1.0]]
        self.assertFalse(curr_rsol.validate())
        

        # Ces séquences devraient être valides:
        curr_rsol.visit_sequence = [[1.0, 2.0, 1.0], [1.0, 3.0, 4.0, 1.0], [1.0, 5.0, 1.0]]
        self.assertTrue(curr_rsol.validate())
        curr_rsol.visit_sequence = [[1.0, 3.0, 4.0, 1.0], [1.0, 2.0, 1.0], [1.0, 5.0, 1.0]]
        self.assertTrue(curr_rsol.validate())


    def test_evaluate(self):
        frp_inst = frp.FastRouteProb(dist_matrix=c)
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
