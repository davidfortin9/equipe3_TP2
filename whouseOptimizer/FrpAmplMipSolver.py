import whouseOptimizer.solver as sl 
import whouseOptimizer.fastroute_problem as frp 
import whouseOptimizer.route_solution as rsol
import amplpy
import sys
import os

class FrpAmplMipSolver(sl.Solver):

    def __init__(self, prob, k, b, d, N):
        super(FrpAmplMipSolver, self).__init__()
        self.prob = prob
        self.k = k
        self.d = d
        self.b = b
        self.N = N


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
            n.set(self.N)

            liste_n = []
            for i in range(1, self.N + 1):
                liste_n.append(i)

            liste_I = []
            liste_J = []
            for i in range(1, self.N+1):
                liste_I.append(i)
                liste_J.append(i)

            # param K
            K = ampl.getParameter('K')
            K.set(self.k)

            # param B
            B = ampl.getParameter('B')
            B.set(self.b)

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
            df.setValues(self.d) 

            ampl.setData(df)
            
            ampl.solve()

            # Extraction de la visit sequence
            x = ampl.getVariable('x').getValues()
            x.val = list(x.getColumn('x.val'))
            x.index0 = list(x.getColumn('index0'))
            x.index1 = list(x.getColumn('index1'))
            sol = x
            Z = (ampl.getObjective('Z').getValues())

            return sol, Z


"""
            start_sequences = []
            count = 0
            for val in x.val[:self.N-1]:
                count = count + 1
                if val == 1:
                    start_sequences.append(count)
    
            #print(visit_sequence_temp)

            
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
            """
        
        