import whouseOptimizer.FrpAmplMipSolver as FrpAmpl
import whouseOptimizer.fastroute_problem as frp
import whouseOptimizer.route_solution as rsol
import whouseOptimizer.frp_rand_solver as frprs
import whouseOptimizer.short_dist_solver as sds
from whouse_modules.pickseq import sku_to_node_pick as sku_to_node_pick
from whouse_modules.pickseq import create_dist_matrix as create_dist_matrix
#import whouse_modules.whouse as wh

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
#        self.dist_matrix = None
        self.whouse = None

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
        self.d = dict(params['d'])
        self.B = int(params['B'])
        self.N = int(params['N'])
#        self.dist_matrix = params['c']
        self.whouse = params['whouse']


        if int(self.solver) == 1 :
            sol, sol_status = self.solveMip()

        elif int(self.solver) == 2 :
            sol, sol_status = self.solveRand()

        elif int(self.solver) == 3:
            sol, sol_status = self.shortDist()  #(frp_inst)   

        return sol, sol_status               

    
    def solveMip(self):
        
        frp_inst = frp.FastRouteProb(dist_matrix=self.data, B=self.B, d=self.d, K=self.K, N=self.N)
        rsol_inst = rsol.Route(solvedProblem=frp_inst, visit_sequence=[])
        
        # Run
        print('Problème actuel:')
        print(str(frp_inst))
        print('Résoudre le problème avec FrpAmplMipSolver')
        frp_solver = FrpAmpl.FrpAmplMipSolver(self.prob)    
        frp_solver.max_time_sec = self.time
        frp_sol = frp_solver.solve()   #.solve (frp_int)


        status = 1

        if rsol.Route.validate(rsol_inst) == False:
            status = 3

        return { 'Route':str(frp_sol), 'Valeur': str(rsol.Route.evaluate(rsol_inst))}, status


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
        if frp_sol.validate(rsol_inst) == False:
            status = 3

        return { 'Route':str(frp_sol), 'Valeur': str(frp_sol.evaluate())}, status          
    
    
    def shortDist(self):

        frp_inst = create_dist_matrix(node_pick, start_node_id, whouse_graph)
        #frp_inst = frp.FastRouteProb(dist_matrix=self.data, B=self.B, d=self.d, K=self.K, N=self.N)
        rsol_inst = rsol.Route(solvedProblem=frp_inst, visit_sequence=[])

        # Run
        print('Problème actuel:')
        print(str(frp_inst))
        print('Résoudre le problème avec le solveur short distance')
        frp_solver = sds.ShortDistance()
        frp_solver.max_time_sec = self.time
        frp_sol = frp_solver.short_dist_solver(frp_inst)

#        rsol_inst = rsol.Route(solvedProblem=frp_inst, visit_sequence=visit_sequence)

        status = 1
        if rsol.Route.validate(rsol_inst) == False:
            status = 3


        return { 'Route':str(frp_sol), 'Valeur': str(rsol.Route.evaluate(rsol_inst))}, status