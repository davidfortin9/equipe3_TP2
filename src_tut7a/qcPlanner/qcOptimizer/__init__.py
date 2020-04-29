from . import frp_rand_solver as frprs
from  . import frp_cp_solver as frpcps
from . import fastroute_problem as frp
from . import route_solution as rsol


class Optimizer:

    def __init__(self):
        self.time = None
        self.verbose = None
        self.solver = None
        self.ampl_path = None
        self.cp_model_path = None
        self.cp_model = None
        self.data = None

    def optimize(self, params):
        
        self.time = float(params['time'])
        self.verbose = int(params['verbose'])
        self.solver = int(params['solver'])
        self.ampl_path = params['ampl_path']
        self.cp_model_path = params['cp_model_path']
        self.cp_model = params['cp_model']
        self.data = params['data']
        

        if int(self.solver) == 1 :
            sol, sol_status = self.solveRandom()

        elif int(self.solver) == 2 :
            sol, sol_status = self.solveCP()

        return sol, sol_status

    def solveRandom(self):
        
        frp_inst = frp.FastRouteProb("Fast route problem", self.data)
        # Run
        print('Problème actuel:')
        print(str(frp_inst))
        print('Résoudre le problème...')
        frp_solver = frprs.FrpRandSolver(self.verbose)
        frp_solver.max_time_sec = self.time
        frp_sol = frp_solver.solve(frp_inst)

        status = 1
        if frp_sol.validate() == False:
            status = 3

        return { 'Route':str(frp_sol), 'Valeur': str(frp_sol.evaluate())} , status

    def solveCP(self):
        frp_inst = frp.FastRouteProb("Fast route problem", self.data)
        print('Résoudre le problème avec un solveur à contrainte')
        frp_solver = frpcps.FrpCpSolver(ampl_path=self.ampl_path,model_path=self.cp_model_path,cp_model=self.cp_model)
        frp_solver.max_time_sec = self.time
        frp_sol = frp_solver.solve(frp_inst)

        is_feasible = frp_sol.validate()
        if frp_sol.proved_optimal and is_feasible:
            status = 0
        elif is_feasible:
            status = 1
        else:
            status = -1

        return { 'Route': str(frp_sol), 'Valeur': str(frp_sol.evaluate())}, status
