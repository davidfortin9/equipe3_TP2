import solver 
import fastroute_problem as frp 
import route_solution as rsol
import amplpy
import sys
import os

class FrpAmplMipSolver(solver.Solver):

    def __init__(self):
        super(FrpAmplMipSolver, self).__init__()

    def __str__(self):
        pass

    def solve(self, prob, K=10, C=150): 
        if type(prob) == frp.FastRouteProb:
            # Création du modèle
            ampl_path = os.path.normpath('C:\Users\maria\Downloads\ampl_mswin64')
            ampl_env = amplpy.Environment(ampl_path)
            ampl = amplpy.AMPL(ampl_env)
            ampl.setOption('solver', 'gurobi')
            ampl.setOption('gurobi_options', 'timelim 2000 outlev 1')
            dir_ampl = os.path.normpath('C:\Users\maria\Desktop\SIAD\equipe3_TP2\equipe3_TP2')
            ampl.read(os.path.join(dir_ampl, 'rock.mod'))

            # Instancier le modèle
            dist_matrix = prob._dist_matrix
            n = len(dist_matrix)
            liste_n = []
            liste_A = []

            #param d
            df = amplpy.DataFrame('d')
            df.setColumn('d', liste_n)
            ampl.setData(df, 'd')

            #param c
            df = amplpy.DataFrame(('A', 'A'), 'c')
            df.setValues({
                (A,A): dist_matrix[i][j]
                for i, A in enumerate(liste_A)
                for j, A in enumerate(liste_A)
                })
            ampl.setData(df)
            ampl.solve()

            # Extraction de la visit sequence
            x = ampl.getVariable('x').getValues()
            x.val = list(x.getColumn('x.val'))
            x.index0 = list(x.getColumn('index0'))
            x.index1 = list(x.getColumn('index1'))
            visit_sequence_temp = []
            print(x)
            count = 0
            for i in x.val:
                if i == 1:
                    visit_sequence_temp.append((x.index0[count], x.index1[count]))
                count = count + 1
            
            # On retourne visit_sequence dans sa forme requise (liste)
            depart = visit_sequence_temp[0][1]
            visit_sequence = []
            visit_sequence.append(visit_sequence_temp[0][1])
            for i in visit_sequence_temp:
                for j in visit_sequence_temp[1:]:
                    if depart == j[0]:
                        depart = j[1]
                        visit_sequence.append(depart)
            sol = rsol.Route()
            sol.visit_sequence = visit_sequence
            Z = (ampl.getObjective('Z').getValues())
        return sol, Z