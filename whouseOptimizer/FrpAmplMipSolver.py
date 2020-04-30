import whouseOptimizer.solver as sl 
import whouseOptimizer.fastroute_problem as frp 
import whouseOptimizer.route_solution as rsol
import amplpy
import sys
import os

class FrpAmplMipSolver(sl.Solver):

    def __init__(self, prob):
        super(FrpAmplMipSolver, self).__init__()
        self.prob = prob

    def __str__(self):
        pass

    def solve(self): 
        if type(self.prob) == frp.FastRouteProb:
            # Création du modèle
            ampl_path = os.path.normpath('C:/Users/David/Documents/AMPL/ampl_mswin64')
            #'C:\Users\maria\Downloads\ampl_mswin64'
            #'C:\\Users\\Utilisateur\\Documents\\BAA\\Hiver 2020\\MQT-2100\\ampl_mswin64 (2)'
            #'C:/Users/David/Documents/AMPL/ampl_mswin64'
            ampl_env = amplpy.Environment(ampl_path)
            ampl = amplpy.AMPL(ampl_env)
            ampl.setOption('solver', 'gurobi')
            ampl.setOption('gurobi_options', 'timelim 2000 outlev 1')
            dir_ampl = os.path.normpath('C:/Users/David/Desktop/equipe3_TP2/equipe3_TP2/Ampl')
            #'C:\Users\maria\Desktop\SIAD\equipe3_TP2\equipe3_TP2'
            #'C:\\Users\\Utilisateur\\Documents\\BAA\\Hiver 2020\\MQT-2100\\Travaux\\TP2\\Git\\Ampl'
            #'C:/Users/David/Desktop/equipe3_TP2/equipe3_TP2'
            ampl.read(os.path.join(dir_ampl, 'VRP.mod'))

            # Instancier le modèle
            dist_matrix = self.prob._dist_matrix
            
            # param n
            n = ampl.getParameter('n')
            n.set(self.prob.N)

            liste_n = []
            for i in range(1, self.prob.N + 1):
                liste_n.append(i)

            liste_I = []
            liste_J = []
            for i in range(1, self.prob.N+1):
                liste_I.append(i)
                liste_J.append(i)

            # param K
            K = ampl.getParameter('K')
            K.set(self.prob.K)

            # param B
            B = ampl.getParameter('B')
            B.set(self.prob.B)

            df = amplpy.DataFrame('I')
            df.setColumn('I', liste_n)
            ampl.setData(df, 'I')
            df = amplpy.DataFrame('J')
            df.setColumn('J', liste_n)
            ampl.setData(df, 'J')

            #param c
            c_dict = dict()
            for i, I in enumerate(liste_I):
                for j, J in enumerate(liste_J):
                    if i != j:
                        # Ajouter au dictionnaire
                        c_dict[(I,J)] = dist_matrix[i][j]
            df = amplpy.DataFrame(('I', 'J'), 'c')
            df.setValues(c_dict)
            ampl.setData(df)

            #param d
            df = amplpy.DataFrame(('I'), 'd')
            df.setValues(self.prob.d) 

            ampl.setData(df)
            
            ampl.solve()

            # Extraction de la visit sequence
            x = ampl.getVariable('x').getValues()

            visit_sequence = []
        
            for row in x:
                l = []
                if row[0] == 1. and row[2] == 1:
                    l.insert(0, 1.)
                    l.insert(1, row[1])
                    visit_sequence.append(l)

            for row in x:
                for r in visit_sequence:
                    if row[0] == r[-1] and row[2] == 1:
                        r.append(row[1])

        return visit_sequence