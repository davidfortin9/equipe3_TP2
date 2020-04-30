"""Usage: python __file__ [OPTIONS]

****************************************************
***********Application gestion d'entrepôt***********
**** Point d'entrée pour tester notre prototype ****


Pour rouler l'application en mode interactif, lancez la sans paramètres:
python __file__

Paramètres obligatoires:
  -c, --config=<F>          Fichier de configuration des solveurs
  -k                        Le nombre de pickers
  -b                        Capacité de transport par picker
  -d                        Quantité de stocks au noeud i
  -N                        Quantité de noeuds

Paramètres optionnels:
  -h, --help                Affiche cette documentation.
  -t, --time=<T>            Temps de résolution maximal en secondes, inscrire 0
                            pour résoudre le problème sans limite de temps,
                            la valeur par défaut est de 10 secondes
  -v, --verbose=<V>         Niveau de verbose, la valeur par défaut est 1
                            0: Aucune sortie
                            1: Sortie minimale
                            2: Sortie détaillée
                            3: Niveau débogage
  -s, --solver=<S>          1:Solveur AmplMip
                            2:Solver Random
                            3:

"""

import getopt
import sys
import os


class Usage(Exception):
   def __init__(self, msg):
      self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv

    # :TODO: Retirer la ligne suivante qui
    # permet de visualiser le contenu de argv
    print(argv)

    params = dict()
    try:
        try:
        
            params['config'] = None
            params['time'] = None
            params['verbose'] = None
            params['config'] = None
            params['solver'] = None
            params['k'] = None
            params['b'] = None
            params['d'] = None
            params['n'] = None
            opts, args = getopt.getopt(argv[1:],
                                    'hc:i:o:t:v:s:k:b:d:N:',
                                    ['help',
                                        'config=',
                                        'in-file=',
                                        'out-file=',
                                        'time=',
                                        'verbose=',
                                        'solver=',
                                        'k=',
                                        'b=',
                                        'd=',
                                        'N='])

            print(opts)
        
            for o, a in opts:
                if o in ("-h", "--help"):
                    print(__doc__)
                    sys.exit(0)
                elif o in ('-c', '--config'):
                    filename = os.path.normpath(a)
                    if not os.path.isfile(filename):
                        raise Usage('Le fichier de configuration est ' +
                                    'inexistant.')
                    params['config'] = a
                elif o in ('-i', '--in-file'):
                    filename = os.path.normpath(a)
                    if not os.path.isfile(filename):
                        raise Usage('Le fichier d\'entré est inexistant.')
                    params['in-file'] = a    
                elif o in ('-o', '--out-file'):
                    filename = os.path.normpath(a)
                    if not os.path.isfile(filename):
                        raise Usage('Le fichier de sortie est inexistant')
                    params['out-file'] = a        
                elif o in ('-t', '--time'):
                    if not a.isnumeric():
                        raise Usage('Le temps alloué en secondes doit ' +
                                     'être numérique.')
                    time = int(a)
                    if time < 0:
                        time = 0
                    params['time'] = time
                elif o in ('-v', '--verbose'):
                    if not a.isnumeric():
                        raise Usage('Le niveau de verbose doit être ' +
                                    'numérique.')
                    verbose = int(a)
                    if verbose < 0:
                        verbose = 0
                    elif verbose > 4:
                        verbose = 4
                    params['verbose'] = verbose
                elif o in ('-s', '--solver'):
                    if not a.isnumeric():
                        raise Usage('Le numéro de solver doit être numérique.')
                    solver = int(a)
                    if solver < 0:
                        solver = 0
                    elif solver > 3:
                        solver = 3
                    params['solver'] = solver
                elif o in ('-k'):
                    if not a.isnumeric():
                        raise Usage('k doit être numérique.')
                    k = int(a)
                    if k < 0:
                        k = 0
                    elif k > 10:
                        k = 10
                    params['k'] = k
                elif o in ('b'):
                    if not a.isnumeric():
                        raise Usage('b doit être numérique.')
                    b = int(a)
                    if b < 0:
                        b = 0
                    elif b > 1000:
                        b = 1000
                    params['b'] = b
                elif o in ('d'):
                    if not a.isnumeric():
                        raise Usage('d doit être numérique.')
                    d = int(a)
                    if d < 0:
                        d = 0
                    elif d > 1000:
                        d = 1000
                    params['d'] = d
                elif o in ('N'):
                    if not a.isnumeric():
                        raise Usage('N doit être numérique.')
                    N = int(a)
                    if N < 0:
                        N = 0
                    elif N > 10:
                        N = 10
                    params['N'] = N                             
                else:
                    print(__doc__)
                    raise Usage('Paramètre invalide')

            # :TODO: Vérifier les paramètres obligatoires ici
            if params['config'] is None:
                raise Usage('Le fichier de configuration est obligatoire.')

            return params
            #return 0

        except getopt.error as msg:
            raise Usage(msg)
    except Usage as err:
        print(err.msg, file=sys.stderr)
        print("Utilisez --help pour afficher la documentation", file=sys.stderr)
        return 2       

if __name__ == "__main__":
    sys.exit(main())        