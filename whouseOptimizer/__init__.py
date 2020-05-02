import whouseOptimizer.FrpAmplMipSolver as FrpAmpl
import whouseOptimizer.fastroute_problem as frp
import whouseOptimizer.route_solution as rsol
import whouseOptimizer.frp_rand_solver as frprs
import whouseOptimizer.short_dist_solver as sds

import os
from whousePortail.utils import Utils
from pathlib import Path

class Optimizer():
    def __init__(self, params=None):
        
        self.time = None
        self.verbose = None
        self.solver = None
        self.ampl_path = None
        self.mip_model_path = None
        self.mip_model = None
        self.data = None
        self.prob = None
        self.K = None
        self.d = None
        self.B = None
        self.N = None

    def optimize(self, params):
        
        self.time = float(params['time'])
        self.verbose = int(params['verbose'])
        self.solver = int(params['solver'])
        self.ampl_path = params['ampl_path']
        self.mip_model_path = params['mip_model_path']
        self.mip_model = params['mip_model']
        self.data = params['data']
#        self.prob = params['prob']
        self.K = int(params['K'])
        d_dict = params['d']
        #self.d = (params['d'])
        d_dict = {int(k):int(v) for k,v in d_dict.items()}
        self.d = d_dict
        self.B = int(params['B'])
        self.N = int(params['N'])


        if int(self.solver) == 1 :
            sol, sol_status = self.solveMip()

        elif int(self.solver) == 2 :
            sol, sol_status = self.solveRand()

        elif int(self.solver) == 3:
            sol, sol_status = self.shortDist()   

        return sol, sol_status               

    
    def solveMip(self):
        
        frp_inst = frp.FastRouteProb(dist_matrix=self.data, B=self.B, d=self.d, K=self.K, N=self.N)
        rsol_inst = rsol.Route(solvedProblem=frp_inst, visit_sequence=[])
        # Run
        print('Problème actuel:')
        print(str(frp_inst))
        print('Résoudre le problème avec FrpAmplMipSolver')
        frp_solver = FrpAmpl.FrpAmplMipSolver(prob=frp_inst)    
        frp_solver.max_time_sec = self.time
        sol = FrpAmpl.FrpAmplMipSolver.solve(frp_solver)
        frp_sol_val = sol[1]
        frp_sol_route = sol[0]
        print(sol)

        status = 1

        if rsol.Route.validate(rsol_inst) == False:
            status = 3

        return { 'Route':str(frp_sol_route), 'Valeur': str(frp_sol_val)}, status


    def solveRand(self):

        frp_inst = frp.FastRouteProb(dist_matrix=self.data, B=self.B, d=self.d, K=self.K, N=self.N)
        rsol_inst = rsol.Route(solvedProblem=frp_inst, visit_sequence=[])

        # Run
        print('Problème actuel:')
        print(str(frp_inst))
        print('Résoudre le problème avec le solveur Random')
        frp_solver = frprs.FrpRandSolver(self.verbose)
        frp_solver.max_time_sec = self.time
        frp_sol = frp_solver.solve(frp_inst)

        status = 1
        if frp_sol.validate() == False:
            status = 3

        return { 'Route':str(frp_sol), 'Valeur': str(frp_sol.evaluate())}, status          
    
    
    def shortDist(self):

        frp_inst = frp.FastRouteProb(dist_matrix=self.data, B=self.B, d=self.d, K=self.K, N=self.N)
        rsol_inst = rsol.Route(solvedProblem=frp_inst, visit_sequence=[])

        # Run
        print('Problème actuel:')
        print(str(frp_inst))
        print('Résoudre le problème avec le solveur short distance')
        frp_solver = sds.ShortDistance(self.prob)
        frp_solver.max_time_sec = self.time
        frp_sol = frp_solver.solve()

        status = 1
        if rsol.Route.validate(rsol_inst) == False:
            status = 3


        return { 'Route':str(frp_sol), 'Valeur': str(rsol.Route.evaluate(rsol_inst))}, status