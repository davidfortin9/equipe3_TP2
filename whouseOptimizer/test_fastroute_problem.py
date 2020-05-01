
import unittest
import whouseOptimizer.fastroute_problem as frp
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
        
        # Puisque les listes sont mutables, j'ai choisis de faire un deepcopy
        # de ma matrice. Je vérifie donc que la matrice conservée en attribut
        # dans mon objet problème est un copie et pas la même que la matrice
        # initiale passée en paramètre.
        self.assertTrue(c is not frp_inst._dist_matrix)

        # Valider le nombre de lieux:
        self.assertEqual(frp_inst.count_locations, 5)
    
