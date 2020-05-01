
import unittest
import whouseOptimizer.fastroute_problem as frp

dist_matrix_small = [[0, 7, 11, 15, 19], 
                    [7, 0, 18, 22, 26],
                    [11, 18, 0, 18, 22],
                    [15, 22, 18, 0, 18],
                    [19, 26, 22, 18, 0]]

class TestFastRouteProb(unittest.TestCase):
    def test_init(self):
        frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix_small)
        
        # Le test suivant permet de s'assuer de l'égalité des deux matrices.
        self.assertTrue(dist_matrix_small == frp_inst._dist_matrix)
        
        # Puisque les listes sont mutables, j'ai choisis de faire un deepcopy
        # de ma matrice. Je vérifie donc que la matrice conservée en attribut
        # dans mon objet problème est un copie et pas la même que la matrice
        # initiale passée en paramètre.
        self.assertTrue(dist_matrix_small is not frp_inst._dist_matrix)

        # Valider le nombre de lieux:
        self.assertEqual(frp_inst.count_locations(), 4)
    
