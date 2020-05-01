import unittest
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

class TestFastRouteProb(unittest.TestCase):
    def test_init(self):
        frp_inst = frp.FastRouteProb(d=d, B=B, N=N, dist_matrix=c, K=K, whouse=None)
        
        # Le test suivant permet de s'assuer de l'égalité des deux matrices.
        self.assertTrue(c == frp_inst._dist_matrix)

        # Valider le nombre de lieux:
        self.assertEqual(frp_inst.count_locations(), 5)
    
