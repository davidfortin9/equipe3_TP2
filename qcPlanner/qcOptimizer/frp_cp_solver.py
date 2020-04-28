from . import solver
from . import fastroute_problem as frp
from . import route_solution as rsol

import numpy as np
import time
import copy

import amplpy
import sys
import os


class MyOutputHandler(amplpy.OutputHandler):
    """
    Classe permettant d'empêcher l'affichage à la console par AMPL.
    """
    def output(self, kind, msg):
        pass


class FrpCpSolver(solver.Solver):

    def __init__(self, ampl_path= None,model_path= None,cp_model=None):
        super(FrpCpSolver, self).__init__()
        self.ampl_path = ampl_path
        self.model_path = model_path
        self.cp_model = cp_model

    def solve(self, prob=None):
        # Préparer l'exécution
        super(FrpCpSolver, self)._prepare()

        # L'exécution est l'appel d'un solveur externe à l'aide de amplpy.
        curr_rsol = rsol.Route(solvedProblem=prob)
        try:
            if self.ampl_path is not None and self.ampl_path != '':
                ampl_path = os.path.normpath(self.ampl_path)
                ampl_env = amplpy.Environment(ampl_path)
                ampl = amplpy.AMPL(ampl_env)
            else:
                ampl_env = amplpy.Environment()

            ampl = amplpy.AMPL(ampl_env)
            
            ampl.setOption('solver', 'ilogcp')


            if self.verbose <= 0:
                output_handler = MyOutputHandler()
                verbose_str = 'quiet'
                ampl.setOutputHandler(output_handler)
            else:
                verbose_str = 'verbose'
            if self.max_time_sec <= 0:
                ampl.setOption('ilogcp_options', 'outlev ' + verbose_str +' optimizer cp')
            else:
                ampl.setOption('ilogcp_options', 'timelimit ' + str(self.max_time_sec) + ' outlev ' + verbose_str +' optimizer cp')
                
            model_dir = os.path.normpath(self.model_path)
            ampl.read(os.path.join(model_dir, self.cp_model))
            
            # Parametres
            param_loc_count = prob.count_locations() 
            set_locations = range(0, param_loc_count)

            # Matrice de distances
            param_dist_matrix = copy.deepcopy(prob._dist_matrix)

            df = amplpy.DataFrame('LOCATIONS')
            df.setColumn('LOCATIONS', set_locations)
            ampl.setData(df, 'LOCATIONS')

            if self.verbose > 1:
                print(str(param_dist_matrix))
                print(str(param_loc_count))
                print(str(set_locations))
                print(str({
                    (i, j):param_dist_matrix[i][j]
                    for i in set_locations
                    for j in set_locations
                }))

            df = amplpy.DataFrame(('source', 'dest'), 'dist')
            df.setValues({
                (i, j):param_dist_matrix[i][j]
                for i in set_locations
                for j in set_locations
            }) 
            ampl.setData(df)

            ampl.solve()

            if self.verbose > 1:
                # Voir ici pour l'interprétation des résultats d'AMPL:
                # https://www.amplstudio.com/tutorials/AMPL%20commands.htm
                print('Status (result): ' + ampl.getObjective('Z').result())
                print('Objective: {}'.format(ampl.getObjective('Z').value()))
                print(type(ampl))
            
            solution = ampl.getVariable('vX').getValues()
            if self.verbose > 0:
                print('Solution: \n' + str(solution))

            # Encoder le vecteur comme une sequence
            for row in solution:
                curr_rsol.visit_sequence.append(int(row[1]))

            # Prouvée optimale?
            if ampl.getObjective('Z').result() == 'solved':
                curr_rsol.proved_optimal = True

        except Exception as e:
            print(e)
            raise


        # Finaliser l'exécution
        super(FrpCpSolver, self)._terminate()

        # Retourner une solution

        return curr_rsol
