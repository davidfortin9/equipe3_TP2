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
        self.k = None
        self.d = None
        self.b = None
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
        self.k = params['k']
        self.d = params['d']
        self.b = params['b']
        self.N = params['N']

        if int(self.solver) == 1 :
            sol, sol_status = self.solveMip()

        elif int(self.solver) == 2 :
            sol, sol_status = self.solveRand()

        elif int(self.solver) == 3:
            sol, sol_status = self.shortDist()   

        return sol, sol_status               

    
    def solveMip(self):
        
        frp_inst = frp.FastRouteProb(self.data)
        # Run
        print('Problème actuel:')
        print(str(frp_inst))
        print('Résoudre le problème avec FrpAmplMipSolver')
        frp_solver = FrpAmpl.FrpAmplMipSolver(self.data, self.k, self.d, self.b, self.N)
        frp_solver.max_time_sec = self.time
        frp_sol = frp_solver.solve()

        status = 1
        #frp_valid = Route.validate(self)
        if rsol.validate() == False:
            status = 3

        return { 'Route':str(frp_sol), 'Valeur': str(frp_sol.evaluate())} , status  


    def solveRand(self):

        frp_inst = frp.FastRouteProb(self.data)
        # Run
        print('Problème actuel:')
        print(str(frp_inst))
        print('Résoudre le problème avec le solveur Random')
        frp_solver = frprs.FrpRandSolver()
        frp_solver.max_time_sec = self.time
        frp_sol = frp_solver.solve(frp_inst)

        status = 1
        if frp_sol.validate() == False:
            status = 3

        return { 'Route':str(frp_sol), 'Valeur': str(frp_sol.evaluate())} , status          
    
    
    def shortDist(self):

        frp_inst = frp.FastRouteProb(self.data)
        # Run
        print('Problème actuel:')
        print(str(frp_inst))
        print('Résoudre le problème avec le solveur short distance')
        frp_solver = sds.ShortDistance(sku_pick=, whouse=, node_pick=, start_node_id=)
        frp_solver.max_time_sec = self.time
        frp_sol = frp_solver.short_dist_solver(frp_inst)

        status = 1
        if frp_sol.validate() == False:
            status = 3

        return { 'Route':str(frp_sol), 'Valeur': str(frp_sol.evaluate())} , status