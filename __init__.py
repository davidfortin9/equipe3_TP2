import FrpAmplMipSolver as FrpAmpl
import fastroute_problem as frp
import route_solution as rsol 
import os
from utils import Utils
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
        self.prob = params['prob']
        self.k = params['k']
        self.d = params['d']
        self.b = params['b']
        self.N = params['N']

        if int(self.solver) == 1 :
            sol, sol_status = self.solveMip()

    
    def solveMip(self):
        
        frp_inst = frp.FastRouteProb(self.prob)
        # Run
        print('Problème actuel:')
        print(str(frp_inst))
        print('Résoudre le problème avec FrpAmplMipSolver')
        frp_solver = FrpAmpl.FrpAmplMipSolver(self.prob, self.k, self.d, self.b, self.N)
        frp_solver.max_time_sec = self.time
        frp_sol = frp_solver.solve()

        status = 1
        if frp_sol.validate() == False:
            status = 3

        return { 'Route':str(frp_sol), 'Valeur': str(frp_sol.evaluate())} , status        
    
    def solveProblem(self):

        if self.data is None:
            if self.params['in-file'] is not None:
                self.load_data(self.params['in-file'])
            else:
                return """
                        Aucune donnée n'est disponible
                    """

        self.params['data']= self.data

    def load_data(self,filename):
        
        filename = os.path.normpath(filename)
        if Path(filename).suffix in ".yaml":
            dict_matrix = Utils.loadYaml(filename)
        elif Path(filename).suffix in ".json":
            dict_matrix = Utils.loadJson(filename)
        elif Path(filename).suffix in ".txt":
            dict_matrix = Utils.loadText(filename)

        # :TODO: Verifier si float crée une erreur: autrefois int
        self.data = [[ float(value) for value in liste] for liste in dict_matrix.values()]

    def set_data(self,data=None):
        self.data = data

    def load_configuration(self,filename):
        self.params = Utils.loadYaml(filename)

    def load_configurations(self,params):
        
        try:
            if params['config'] is not None:
                self.config_filename = params['config']
                self.params = Utils.loadYaml(self.config_filename)
                
        except KeyError:
            pass
        
        try:
            if params['solver'] is not None :
                self.params['solver'] = params['solver']
                
        except KeyError:
            pass
        try:
            if params['time'] is not None :
                self.params['time'] = float(params['time'])
        except KeyError:
            pass

        try:
            if params['in-file'] is not None:
                self.params['in-file'] = params['in-file']
        except KeyError:
            pass
        try:
            if params['out-file'] is not None:
                self.params['out-file'] = params['out-file']
        except KeyError:
                pass
        try:
            if params['verbose'] is not None:
                self.params['verbose'] = int(params['verbose'])
        except KeyError:
            pass
        try:
            if params['ampl_path'] is not None:
                self.params['ampl_path'] = params['ampl_path']
        except KeyError:
            pass

        try:
            if params['cp_model_path'] is not None:
                self.params['cp_model_path'] = params['cp_model_path']
        except KeyError:
            pass

        try:
            if params['cp_model'] is not None:
                self.params['cp_model'] = params['cp_model']
        except KeyError:
            pass

    def get_data(self,row,col):
        if self.data is None:
            return
        return self.data[row][col]

    '''def show_solution(sol):
  
        print("\n\n Meilleure route obtenue\n\n" + 50*"*")
        for (key, val) in sol.items():
            print('\t' + key )
            print('\t' + val)
            print(50 * '*')'''