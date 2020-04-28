'''Point d'entrée pour les tests en lots. Tous ce passe à partir du fichier __init__ dans
    le dossier whousePortail'''

import sys


def get_route(params):
    objSync = init.Optimizer(params=params)
    solution = objSync.solveProblem()
    #show_solution(solution)

if __name__ == '__main__':
    print('\n' + 50*'*')
    print('***** Outil de planification des picks *****')
    print(50*'*'+'\n')
    get_route(main())

#if __name__ == "__main__":
#    sys.exit(main())

