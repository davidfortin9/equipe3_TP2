import subprocess
import os

'''On test 5 instances sur un petit entrepôt, d'une matrice de taille 8x8'''

#size_nos = range(4,8)
instance_nos = range(1,6)
#for size_no in size_nos:
for instance_no in instance_nos:
    command_line = ['python',
                    'main.py',
                    '-c',
                    'data/petit_entrepot/config_mip_size8_inst' + str(instance_no) + '.yaml'
                    ]
    print(command_line)
    subprocess.run(command_line)
