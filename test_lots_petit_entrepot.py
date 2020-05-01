import subprocess
import os

'''Tests de toutes les instances, pour tous les pickers et tous les solveurs pour le 
    petit entrepôt.'''

solveur_nos = range(1,4)
size_nos = 8
instance_nos = range(1,6)
pick_nos = range(1,5)
for solveur_no in solveur_nos:
    for pick_no in pick_nos:
        for instance_no in instance_nos:
            
            command_line = ['python',
                            '__main__.py',
                            '-c',
                            'data/petit_entrepot/config_solveur_size' + 
                                str(size_nos) + '_' + 'inst' + str(instance_no) + '.yaml',
                            '-s' + str(solveur_no),    
                            '-K' + str(pick_no),
                            '-o',
                            'data/resultats/petit_entrepot/solveur' + str(solveur_no) + 
                                '_size8_inst1_sol.out'
                            ]
            print(command_line)
            subprocess.run(command_line)
