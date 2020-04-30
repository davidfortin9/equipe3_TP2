import subprocess
import os

'''On test 5 matrices de taille 50 x 50 (gros entrepôt) pour notre solver amplmip'''

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
