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

    def solve(self, prob): 
        if type(prob) == frp.FastRouteProb:
            # Création du modèle
            ampl_path = os.path.normpath('C:/Users/David/Documents/AMPL/ampl_mswin64')
            ampl_env = amplpy.Environment(ampl_path)
            ampl = amplpy.AMPL(ampl_env)
            ampl.setOption('solver', 'gurobi')
            ampl.setOption('gurobi_options', 'timelim 600 outlev 1')
            dir_ampl = os.path.normpath('C:/Users/David/Desktop/equipe7_TP1/equipe7_TP1/q2')
            ampl.read(os.path.join(dir_ampl, 'question2.mod'))

            # Instancier le modèle
            dist_matrix = prob._dist_matrix
            r = len(dist_matrix)
            liste_I = []
            liste_J = []
            liste_K = []
            l = ampl.getParameter('l')
            l.set(r)
            for i in range(2, r+1):
                liste_K.append(str(i))
                
            for i in range(1, r+1):
                liste_I.append(str(i))
                liste_J.append(str(i))
            df = amplpy.DataFrame('K')
            df.setColumn('K', liste_K)
            ampl.setData(df, 'K')
            df = amplpy.DataFrame('I')
            df.setColumn('I', liste_I)
            ampl.setData(df, 'I')
            df = amplpy.DataFrame('J')
            df.setColumn('J', liste_J)
            ampl.setData(df, 'J')
            df = amplpy.DataFrame(('I', 'J'), 'D')
            df.setValues({
                (I,J): dist_matrix[i][j]
                for i, I in enumerate(liste_I)
                for j, J in enumerate(liste_J)
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
        return sol

    def getobjective(self, prob):
        if type(prob) == frp.FastRouteProb:
            # Création du modèle
            ampl_path = os.path.normpath('C:/Users/David/Documents/AMPL/ampl_mswin64')
            ampl_env = amplpy.Environment(ampl_path)
            ampl = amplpy.AMPL(ampl_env)
            ampl.setOption('solver', 'gurobi')
            ampl.setOption('gurobi_options', 'timelim 600 outlev 1')
            dir_ampl = os.path.normpath('C:/Users/David/Desktop/equipe7_TP1/equipe7_TP1/q2')
            ampl.read(os.path.join(dir_ampl, 'question2.mod'))

            # Instancier le modèle
            dist_matrix = prob._dist_matrix
            r = len(dist_matrix)
            liste_I = []
            liste_J = []
            liste_K = []
            l = ampl.getParameter('l')
            l.set(r)
            for i in range(2, r+1):
                liste_K.append(str(i))
                
            for i in range(1, r+1):
                liste_I.append(str(i))
                liste_J.append(str(i))
            df = amplpy.DataFrame('K')
            df.setColumn('K', liste_K)
            ampl.setData(df, 'K')
            df = amplpy.DataFrame('I')
            df.setColumn('I', liste_I)
            ampl.setData(df, 'I')
            df = amplpy.DataFrame('J')
            df.setColumn('J', liste_J)
            ampl.setData(df, 'J')
            df = amplpy.DataFrame(('I', 'J'), 'D')
            df.setValues({
                (I,J): dist_matrix[i][j]
                for i, I in enumerate(liste_I)
                for j, J in enumerate(liste_J)
                })
            ampl.setData(df)
            ampl.solve()
            Z = (ampl.getObjective('Z').getValues())
        return Z
        #Test P-O