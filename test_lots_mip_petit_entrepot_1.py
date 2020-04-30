import subprocess
import os

'''On test 5 matrices de taille 8 x 8 (petit entrepôt) pour notre solver amplmip'''

size_nos = (8,50)
instance_nos = range(1,6)
pick_nos = range(1,5)
for size_no in size_nos:
    for instance_no in instance_nos:
        for pick_no in pick_nos:
            command_line = ['python',
                            'main.py',
                            '-c',
                            'data/config_mip_size' + str(size_no) + '_' +
                            'inst' + str(instance_no) + '.yaml',
                            '-k' + str(pick_no)
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
