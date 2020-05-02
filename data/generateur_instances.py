import yaml
import numpy as np


def gen_random_instance(n=3,
                        min_value=0.,
                        max_value=20.):
    my_matrix = np.random.randint(low=min_value,
                                  high=max_value,
                                  size=(n, n))
    my_sym_matrix = (my_matrix + my_matrix.T) // 2
    my_sym_matrix[range(n), range(n)] = 0
    return my_sym_matrix

def dump_instance_yaml(matrix = None,
                       filename = 'inst.yml'):
    dict_dist_matrix = dict()
    for i_row, row in enumerate(matrix):
        dict_dist_matrix[i_row+1] = row.tolist()

    with open(filename, 'w') as f:
        yaml.dump(dict_dist_matrix, f)

        

np.random.seed(253785)
for inst_size in range(16, 17):
    for rand_inst_no in range (1, 6):
        instance = gen_random_instance(n=inst_size,
                                        min_value=0.,
                                        max_value=20.)
        instance_filename = 'mip' + '_size' + str(inst_size) \
            + '_inst' + str(rand_inst_no) + '.yaml'
        dump_instance_yaml(matrix=instance,
                            filename=instance_filename)    

