import random
import networkx as nx
import numpy as np

class RJ():
    def __init__(self):
        self.G1 = nx.Graph()

    def rj(self, complete_graph, nodes_to_sample):

        list_nodes = list(complete_graph.nodes())
        nr_nodes = len(complete_graph.nodes())
        upper_bound_nr_nodes_to_sample = nodes_to_sample
        index_of_first_random_node = random.randint(0, nr_nodes-1)

        sampled_graph = []
        sampled_graph.append(list_nodes[index_of_first_random_node])

        while len(sampled_graph) < upper_bound_nr_nodes_to_sample:
            index_of_new_node = random.randint(0, nr_nodes - 1)
            if list_nodes[index_of_new_node] not in sampled_graph:
                new_node = index_of_new_node
            else:
                continue
            p = random.random()
            choice = np.random.choice(['prev', 'neigh'], 1, p=[1 - p, p])
            if choice == 'neigh':
                sampled_graph.append(list_nodes[new_node])

        print(sampled_graph)
        tmp = nx.Graph()
        tmp.add_nodes_from(sampled_graph)
        self.G1 = complete_graph.subgraph(tmp.nodes())

        return self.G1
