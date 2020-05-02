import subprocess
import os

'''Tests de toutes les instances, pour tous les pickers et tous les solveurs pour le 
    gros entrepôt.'''

solveur_nos = range(1,4)
size_nos = 16
instance_nos = range(1,6)
for solveur_no in solveur_nos:
    for instance_no in instance_nos:        
        command_line = ['python.exe',
                        '__main__.py',
                        '-c',
                        'data/gros_entrepot/config_solveur_size' + 
                            str(size_nos) + '_' + 'inst' + str(instance_no) + '.yaml',
                        '-s' + str(solveur_no)
                        ]
        print(command_line)
        subprocess.run(command_line)
