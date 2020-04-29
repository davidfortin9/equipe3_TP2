import subprocess
import os

instance_nos = range(1,5)
for instance_no in instance_nos:
    command_line = ['python',
                    'main.py',
                    '-c', 
                    'data/config_cp_inst' + str(instance_no) + '.yaml'
                   ]
    print(command_line)
    subprocess.run(command_line)
