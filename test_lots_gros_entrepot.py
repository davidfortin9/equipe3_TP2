import subprocess
import os

'''Tests de toutes les instances, pour tous les pickers et tous les solveurs pour le 
    gros entrepôt.'''

solveur_nos = range(1,4)
size_nos = 50
instance_nos = range(1,6)
pick_nos = range(1,5)
for solveur_no in solveur_nos:
    for pick_no in pick_nos:
        for instance_no in instance_nos:
            
            command_line = ['python',
                            '__main.py__',
                            '-c',
                            'data/gros_entrepot/config_solveur' + str(solveur_no) + '_size' + 
                                str(size_nos) + '_' + 'inst' + str(instance_no) + '.yaml',
                            '-k' + str(pick_no)
                            ]
            print(command_line)
            subprocess.run(command_line)