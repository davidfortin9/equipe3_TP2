import json
import yaml
import sys
from pathlib import Path
import os
import datetime

from .utils import Utils

from whouseOptimizer import Optimizer as Opt


class WhouseSync():
    def __init__(self, params=None):
        
        self.solveur = Opt()
        self.data = None
        self.is_data_saved = False 
        self.data_filename = None     
        self.config_filename = None
        self.params = dict()
        self.initParams()
        
        if params is not None:
            self.load_configurations(params)
        
        # :TODO: Remplacer par un fichier unique pour toutes les instances?
        #self.result_file = os.path.join(self.params['result-folder'], os.path.basename(self.params['in-file']).split('.')[0]+'.csv')
        self.result_file = os.path.join(self.params['result-folder'], 'experiments.csv')
        del self.params['result-folder']

    def initParams(self):
        self.params['config'] = None
        self.params['solver'] = None
        self.params['time'] = None
        self.params['in-file'] = None
        self.params['out-file'] = None
        self.params['verbose'] = None
        self.params['ampl_path'] = None
        self.params['mip_model'] = None
        self.params['mip_model_path'] = None
#        self.params['d'] = None
#        self.params['B'] = None
#        self.params['K'] = None
#        self.params['N'] = None
        self.params['whouse'] = None

    def solveProblem(self):

        if self.data is None:
            if self.params['in-file'] is not None:
                self.load_data(self.params['in-file'])
#            if self.params['whouse'] is not None:   #Ajout pour voir si whouse load
#                self.load_data(self.params['whouse'])    
            else:
                return """
                    Aucune donnée n'est disponible
                """

        self.params['data']= self.data

        self.sol, self.sol_status = self.solveur.optimize(self.params)
        
        # Save solution in a file
        
        if self.params['out-file'] is not  None:
            Utils.dumpYaml(self.sol, self.params['out-file'])

        append_to_existing_file = os.path.isfile(self.result_file)
        Utils.dumpCsv(self.params,
                      self.sol_status,
                      self.sol['Valeur'],
                      filename = self.result_file,
                      append=append_to_existing_file)
        return self.sol
        
    def load_data(self,filename):
        
        filename = os.path.normpath(filename)
        if Path(filename).suffix in ".yaml":
            dict_matrix = Utils.loadYaml(filename)
        elif Path(filename).suffix in ".json":
            dict_matrix = Utils.loadJson(filename)
        elif Path(filename).suffix in ".txt":
            dict_matrix = Utils.loadText(filename)
#        elif Path(filename).suffix in '.py':
#            dict_matrix = (filename) #Ajout pour voir si whouse load    

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
            if params['whouse'] is not None:
                self.params['whouse'] = params['whouse']
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
            if params['mip_model_path'] is not None:
                self.params['mip_model_path'] = params['mip_model_path']
        except KeyError:
            pass

        try:
            if params['mip_model'] is not None:
                self.params['mip_model'] = params['mip_model']
        except KeyError:
            pass
    
    def get_data(self,row,col):
        if self.data is None:
            return
        return self.data[row][col]

    def get_nb_customers(self):
        if self.data is None:
            return 0
        else:
            return len(self.data)