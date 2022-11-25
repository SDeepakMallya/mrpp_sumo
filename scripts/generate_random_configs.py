import networkx as nx
import sys
import rospkg
import random as rn
import tpbp_functions as fn
import os
if __name__ == '__main__':
    dir_name = rospkg.RosPack().get_path('mrpp_sumo')
    if len(sys.argv[1:]) == 0:
        graph_name = ['grid_5_5','cair','iitb']
        #graph_name = ['st_line']
        multiplicity = 3
        num_priority=[4,5,6]
        #alg_ids = [6, 7, 8, 9]
        algo_name = ['ppa_greedy']
        vel = 10.
        parameters=" ".join([])
        # prior_nodes = ['0', '4', '20', '24']
        # min_tp = fn.compute_min_tp(graph, prior_nodes)/vel
        # min_tp = 40.
        # lambda_priors = [0.0]
        # len_walks = [40, 80, 120]
        # max_divisions = 10
        # eps_prob = 0
        # max_bots = 6
        # threads = 10
        # episodes = 5000
        init_bots = list(range(1, 5))
        sim_length = 20000
        # discount_factors = [1]
        i = 0
        for _ in range(multiplicity):
            for g in graph_name:        # selectin a graph from 3 graphs  ##1
                graph = nx.read_graphml(dir_name + '/graph_ml/' + g + '.graphml')
                for a in num_priority:      ##2
                    prior_nodes = rn.sample(graph.nodes(), a)
                    for ib in init_bots:            #number of bots 1,2,3,4 ## 3
                        i += 1
                        loc=rn.sample(prior_nodes,ib)
                        # min_tp=(fn.compute_min_tp(graph,prior_nodes))/vel
                        for algo in algo_name:
                            if not os.path.isdir(dir_name + '/config/' + algo + '/depth_0'):
                                os.mkdir(dir_name + '/config/' + algo + '/depth_0')
                            with open(dir_name + '/config/' + algo + '/depth_0/{}_{}_{}_0.yaml'.format(algo,g,i), 'w') as f:
                                f.write('use_sim_time: true\n')
                                f.write('graph: {}\n'.format(g))
                                f.write('init_bots: {}\n'.format(ib))
                                f.write('priority_nodes: {}\n'.format(' '.join(list(map(str,prior_nodes)))))
                                f.write('init_locations: \'{}\'\n'.format(' '.join(loc)))
                                f.write('done: false\n')
                                f.write('sim_length: {}\n'.format(sim_length))
                                f.write('random_string: {}_{}_{}_0\n'.format(algo,g,i))
                                f.write('algo_name: {}\n'.format(algo))
                                # if algo == 'tpbp_alt1':
                                f.write('parameters: \'0\'')
                        print (i,"Yeh i hai")
    else:
        print ('Please pass the appropriate arguments')