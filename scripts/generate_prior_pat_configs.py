#!/bin/usr/env python3

'''
A script to generate configs based on the parameters required

Output:
appropriate yaml files in config directory
'''

import sys, os
import numpy
import rospkg
import random as rn
import tpbp_functions as fn
import glob 
import yaml

if len(sys.argv[1:]) == 0:
    print('Specify Algorithm and corresponding parameters')   
else:
    alg_name = sys.argv[1]
    parameters = sys.argv[2:]
    dirname = rospkg.RosPack().get_path('mrpp_sumo')
    file_str = 'prior_pat_configs'
    dirname += '/config/'


    conf_files = glob.glob(dirname  + '{}/depth_0/*'.format('ppa_greedy'))
    print(dirname  + '{}/depth_0/*'.format('ppa_greedy'))
    i = 0
    count = 0
    for c in conf_files:
        # print(c)
        with open(c, 'r') as f:
            p = yaml.safe_load(f)
        p['algo_name'] = alg_name
        n = len(p['priority_nodes'].split(' '))
        p['parameters'] = ' '.join(parameters) + " {}".format(numpy.ceil(n/2))
        i = c.split("_")[-2]
        name_add = '_'.join(parameters)
        p['random_string'] = alg_name + '_' + p['graph'] + '_' + str(i) + '_' + name_add
        dir_path = dirname + alg_name + '/depth_' + name_add
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)

        with open(dirname + alg_name + '/depth_' + name_add + '/{}.yaml'.format(p['random_string']), 'w') as f:
            cur = yaml.dump(p, f)\
            # break
        count += 1
        print(count)