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
                            '__main.py__',
                            '-c',
                            'data/petit_entrepot/config_solveur_size' + 
                                str(size_nos) + '_' + 'inst' + str(instance_no) + '.yaml',
                            '-s' + str(solveur_no),    
                            '-K' + str(pick_no)
                            ]
            print(command_line)
            subprocess.run(command_line)

#size_nos = range(4,8)
#instance_nos = range(1,6)
#for size_no in size_nos:
#for instance_no in instance_nos:
#    command_line = ['python',
#                    '__main__.py',
#                    '-c',
#                    'data/petit_entrepot/config_mip_size8_inst' + str(instance_no) + '.yaml'
#                    ]
                    #TODO: Automatiser le numéro de size, le numéro d'instance,
                    #le numéro de pick et le numéro de solver. Le numéro de pick pourra être
                    #automatiser dans le paramètre -k et le numéro de solver dans -s.
#    print(command_line)
#    subprocess.run(command_line)
