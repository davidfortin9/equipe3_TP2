"""Usage: python __file__ [OPTIONS]
Lance l'application Quantum Courrier en lignes de commandes.
L'application permet d'exécuter des tests en lots ou de résoudre un problème de distribution unique.

Pour rouler l'application en mode interactif, lancez la sans paramètres:
python __file__

Paramètres obligatoires:
  Aucun

Paramètres optionnels:
  -c, --config              Fichier de configuration des solveurs
  -i, --in-file             Fichier d'instance en entrée
  -o, --out-file            Fichier de sortie pour les résultats
  -s, --solver              Identifiant numérique du solveur, 
                            la valeur par défaut est 1
                            1: Random solver 
                            2: CP solver
  -t, --time                Temps de résolution maximal en secondes, inscrire 0
                            pour résoudre le problème sans limite de temps,
                            la valeur par défaut est de 10 secondes
  -v, --verbose             Niveau de verbose, la valeur par défaut est 1
                            0: Aucune sortie
                            1: Sortie minimale
                            2: Sortie détaillée
                            3: Niveau débogage

"""

import getopt
import sys
import os
from pathlib import Path 

from qcPlanner.qcSync.utils import Utils
from qcPlanner.qcSync.config import Config


class Usage(Exception):
   def __init__(self, msg):
      self.msg = msg

def get_params_from_cli(argv=None):
   """
      QcPlanner....
      python main.py [-h:(help)] [-c: configuration file] [-i: input file] [-o: output file] [-s: solver type] [-t: time] [-v: verbose]
   """
   if argv is None:
      argv = sys.argv

   params = dict()
   try:
       
      in_dir = None
      out_dir = None
      params['time'] = None
      params['verbose'] = None
      params['config'] = None
      opts, args = getopt.getopt(
         argv[1:],
         'hc:i:o:s:t:v:',
         ['help',
               'config',
               'in-file=',
               'out-file=',
               'solver='
               'time=',
               'verbose=']) 
   
      for o, a in opts:
         if o in ("-h", "--help"):
               print(__doc__)
               sys.exit(0)
         elif o in ('-c','--config'):
               Utils.checkFileInput(a)
               params['config'] = a
         elif o in ('-i', '--in-file'):
               Utils.checkFileInput(a)
               params['in-file'] = a
         elif o in ('-o', '--out-file'):
               params['out-file'] = a
         elif o in ('-s', '--solver'):
               Utils.checkNumericInput(a,1,2)
               params['solver'] = a
         elif o in ('-t', '--time'):
               Utils.checkNumberInput(a)
               params['time'] = a
         elif o in ('-v', '--verbose'):
               Utils.checkNumericInput(a,0,3)
               params['verbose'] = int(a)
         else:
               print(__doc__)
               raise Usage('Invalid argument')

      return params

   except getopt.error as msg:
      raise Usage(msg)


def get_params_from_user(argv=None):
   """
      QcPlanner....\n
      suivez directement les instructions à l'écran pour choisir les options appropriées.
   """
   params = dict()

   loop_exit = 'o'

   while loop_exit in ['o','O']:

      choice_option = input(""" Menu des options\n
      1: Fichier de configuration \n
      2: Fichier d'entrée \n
      3: Fichier de sortie \n
      4: Solveur \n
      5: Veuillez choisir le temps de résolution maximal en secondes\n
      6: Niveau de détails pour la sortie console \n
      0: Choisir les options par défaut\n
      """ )
      
      choice_option = Utils.checkNumericInput(choice_option, 0, 6)
      
      if choice_option == 0:
         return Utils.loadYaml(Config.DEFAULT_CONFIG_FILE)

      if choice_option == 1:
         params['config'] = input("Choisissez un fichier de configuration: ")
         params['config'] = Utils.checkFileInput(params['config'])
      
      if choice_option == 2:
         params['in-file'] = input("Choisissez un fichier d'entrée: ")
         params['in-file'] = Utils.checkFileInput(params['in-file'])
      
      if choice_option == 3:
         params['out-file'] = input("Choisissez un fichier de sortie: ")
      
      if choice_option == 4:
         params['solver'] = input("Veuillez choisir le solveur à utiliser:\n 1: Random solver | 2: CP solver\n")
         params['solver'] = Utils.checkNumericInput(params['solver'], 1, 2)
         if  params['solver'] in [2]:
               print("Vous avez choisi un modele exact")
               filepath= input("""Veuillez fournir le fichier contenant le modèle\n""" )
               filepath = Utils.checkFileInput(filepath, ['.mod'])
               if params['solver'] == 2:
                  params['cp_model_path'], params['cp_model'] = os.path.split(filepath)
               
               filepath = input("""Veuillez fournir le dossier d'installation d'AMPL \n""" )
               filepath = Utils.checkPathInput(filepath)
               params['ampl_path'] = filepath
               
      if choice_option == 5:
         params['time'] = input("Veuillez choisir le temps d'exécution en secondes \n inscrire 0 pour résoudre le problème sans limite de temps\n")
         params['time'] = Utils.checkNumericInput(params['time'], 0, 7200)
         if params['time'] == 0:
            params['time'] = int(sys.float_info.max)

      if choice_option == 6:
         print("Veuillez choisir le niveau de détails pour la sortie console.")
         prompt = """
            #   0: Aucune sortie
            #   1: Sortie minimale
            #   2: Sortie détaillée
            #   3: Niveau débogage
         Entrer le niveau désiré entre 0 et 3:
         """

         params['verbose'] = input(prompt)

         params['verbose'] = Utils.checkNumericInput(params['verbose'], 0, 3)
      

      loop_exit = input("""Voulez-vous choisir une autre option pour le solveur\n
      o, O pour Oui | n, N pour Non \n""")
      loop_exit = Utils.checkCharInput(loop_exit,['o','O','n','N'])
         
   return params
   

def show_solution(sol):
  
   print("\n\n Meilleure route obtenue\n\n" + 50*"*")
   for (key, val) in sol.items():
      print('\t' + key )
      print('\t' + val)
   print(50 * '*')
   
def prompt_menu():
      
   print("\n Les options par défaut du solveur sont:\n")
   default_config = Utils.loadYaml(Config.DEFAULT_CONFIG_FILE)
   for key, val in default_config.items():
      print(key.upper() + ': ' + val.upper())
   
   change = input("\nDésirez-vous changer ces options par défaut? \nEntrer 1 pour oui, 0 pour non \n ")
   change = Utils.checkNumericInput(change,0, 1)
   
   return change, default_config

if __name__ == "__main__":
    sys.exit(prompt_menu())
    
