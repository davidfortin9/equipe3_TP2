import whouseOptimizer.FrpAmplMipSolver as FrpAmpl
import whouseOptimizer.fastroute_problem as frp
import whouseOptimizer.route_solution as rsol 
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
        if frp_sol.validate() == False:
            status = 3

        return { 'Route':str(frp_sol), 'Valeur': str(frp_sol.evaluate())} , status        
    
    #TODO: Coder pour le solver random ou heuristique
    #TODO: Coder pour le solver GOOGLE OR TOOLS