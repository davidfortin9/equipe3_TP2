import subprocess
import os

'''On test 5 instances sur un gros entrepôt, d'une matrice de taille 50x50'''

size_nos = range(4,8)
instance_nos = range(1,4)
for size_no in size_nos:
    for instance_no in instance_nos:
        command_line = ['python',
                        'main.py',
                        '-c',
                        'data/config_mip_size' + str(size_no) + '_' +
                        'inst' + str(instance_no) + '.yaml'
                        ]
        print(command_line)
        subprocess.run(command_line)
