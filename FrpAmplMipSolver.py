import solver 
import fastroute_problem as frp 
import route_solution as rsol
import amplpy
import sys
import os

class FrpAmplMipSolver(solver.Solver):

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
            ampl_env = amplpy.Environment(ampl_path)
            ampl = amplpy.AMPL(ampl_env)
            ampl.setOption('solver', 'gurobi')
            ampl.setOption('gurobi_options', 'timelim 2000 outlev 1')
            dir_ampl = os.path.normpath('C:/Users/David/Desktop/equipe3_TP2/equipe3_TP2')
            ampl.read(os.path.join(dir_ampl, 'VRP.mod'))

            # Instancier le modèle
            dist_matrix = self.prob._dist_matrix
            
            # param n
            n = ampl.getParameter('n')
            n.set(self.N)

            liste_n = [1,2,3,4,5,6,7]
            

            liste_n0 = []
            for i in range(0, self.N + 1):
                liste_n0.append(i)

            print(liste_n)
            print(liste_n0)
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
            df = amplpy.DataFrame(('I', 'J'), 'c')
            df.setValues({
                (I,J): dist_matrix[i][j]
                for i, I in enumerate(liste_n0)
                for j, J in enumerate(liste_n0)
                })

            #param d
            df = amplpy.DataFrame('d')
            df.setValues(for i in self.d.keys():
            {()})

            ampl.setData(df)
            print(df)

            ampl.solve()

            # Extraction de la visit sequence
            x = ampl.getVariable('x').getValues()
            x.val = list(x.getColumn('x.val'))
            x.index0 = list(x.getColumn('index0'))
            x.index1 = list(x.getColumn('index1'))
            visit_sequence_temp = []
            print(x)
            """
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
        """