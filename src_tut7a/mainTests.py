import unittest
import sys

import qcPlanner.qcOptimizer.frp_rand_solver as frprs
import qcPlanner.qcOptimizer.frp_cp_solver as frpcs
import qcPlanner.qcOptimizer.fastroute_problem as frp
import qcPlanner.qcOptimizer.route_solution as rsol
from qcPlanner.qcSync.QcSync import QcSync
from qcPlanner.qcSync.config import Config

class TestSolver(unittest.TestCase):

      def setUp(self):
            """
            Test solver
            """
            self.sync = QcSync()
            self.FILENAME = "defaultData/default_instance.yaml"

            self.matrix = [[0,  20,  30, 40],
                  [20,  0,  30,  5],
                  [30, 30,   0, 10],
                  [40,  5,  10,  0]]
            self.sequence1 = [0, 2, 3]
            self.sequence2 = [1, 1, 1, 1]
            self.sequence3 = [0, 1, 2, 3]
            self.sequence4 = [0, 2, 1, 3]
            self.sequence5 = [0, 2, 3]

      def test_loadYaml(self):
            """
            Test if yaml file is loaded successfully
            and converted in array
            """
            self.sync.load_data(self.FILENAME)
            self.matrix = self.sync.data
            print(self.matrix)
      
      def test_distanceMatrix(self):
            """
            Test the distance matrix
            """
            self.sync.load_data(self.FILENAME)
            self.matrix = self.sync.data
            frp_inst = frp.FastRouteProb(dist_matrix=self.matrix)
            print(str(frp_inst))

      def test_showSolution(self):

            self.matrix = self.sync.load_data(self.FILENAME)
            frp_inst = frp.FastRouteProb(dist_matrix=self.matrix)

            print('\n La solution devrait s\'afficher:')
            curr_rsol = rsol.Route(solvedProblem=frp_inst)
            curr_rsol.visit_sequence = self.sequence1
            print(str(curr_rsol))
      
      def test_route(self):
            """
            '*** Tests Route ***'
            """
            self.sync.load_data(self.FILENAME)
            self.matrix = self.sync.data
            frp_inst = frp.FastRouteProb(dist_matrix=self.matrix)

            curr_rsol = rsol.Route(solvedProblem=frp_inst)

            print('La séquence initiale devrait être invalide:')
            self.assertFalse(curr_rsol.validate())
            
            print('La séquence [0, 2, 3] devrait être invalide:')
            curr_rsol.visit_sequence = self.sequence1
            self.assertFalse(curr_rsol.validate())
             
            print('La séquence [1, 1, 1, 1] devrait être invalide:')
            curr_rsol.visit_sequence = self.sequence2
            
            self.assertFalse(curr_rsol.validate())
           
            print('La séquence [0, 1, 2, 3] devrait être valide:')
            curr_rsol.visit_sequence = self.sequence3
            self.assertTrue( curr_rsol.validate())
            
            print('La séquence [0, 2, 1, 3] devrait être valide:')
            curr_rsol.visit_sequence = self.sequence4
            self.assertTrue( curr_rsol.validate())
            
            print('La valeur de la fonction objectif pour [0, 2, 3]',
                  ' devrait être un grand nombre:')
            curr_rsol.visit_sequence = self.sequence1
            self.assertIs(curr_rsol.evaluate(),sys.float_info.max)
            
            print('La valeur de la fonction objectif pour [0, 2, 1, 3] devrait être 65:')
            curr_rsol.visit_sequence = self.sequence4
            print(curr_rsol.evaluate())
            """
            self.assertIs(curr_rsol.evaluate(), 65)
     
            """
      
      def test_solver(self):
            """
            *** Tests frp_rand_solver ***
            """
            frp_inst = frp.FastRouteProb(dist_matrix=self.matrix)
            print('Retourne une solution sans afficher de sortie:')
            frp_solver = frprs.FrpRandSolver()
            frp_solver.max_time_sec = 3
            frp_solver.verbose = 0
            frp_sol = frp_solver.solve(frp_inst)
            print('Solution retournée: ' + str(frp_sol))
            print('Objectif: ' + str(frp_sol.evaluate()))
      
      def test_loadDefault_config(self):
            """
                  Load default configuration
            """
            self.sync.load_configuration(Config.TEST_CONFIG_FILE)
            self.params = self.sync.params

      def test_CpSolver(self):
            """
            *** Tests frp_cp_solver ***
            """
            frp_inst = frp.FastRouteProb(dist_matrix=self.matrix)
            # Load configuration
            self.test_loadDefault_config()
           
            frp_solver = frpcs.FrpCpSolver(ampl_path=self.params['ampl_path'],model_path=self.params['cp_model_path'],cp_model=self.params['cp_model'])
            frp_solver.max_time_sec = 3
            frp_solver.verbose = 1
            frp_sol = frp_solver.solve(frp_inst)
            print('Solution retournée: ' + str(frp_sol))
            print('Objectif: ' + str(frp_sol.evaluate()))

if __name__ == "__main__":      
      unittest.main()

