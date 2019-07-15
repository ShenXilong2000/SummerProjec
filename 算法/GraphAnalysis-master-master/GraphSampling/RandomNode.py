import random
import networkx as nx

class RandomNode():

    def __init__(self):
        self.G1 = nx.Graph()

    def randomnode(self, G, size):
        list_nodes = list(G.nodes())

        nr_nodes = len(list_nodes)
        upper_bound_nr_nodes_to_sample = size

        sampled_graph = []
        sampled_graph_edges = []

        while (len(sampled_graph) < upper_bound_nr_nodes_to_sample):
            index_of_first_random_node = random.randint(0, nr_nodes - 1)
            if list_nodes[index_of_first_random_node] in sampled_graph:
                continue
            else:
                sampled_graph.append(list_nodes[index_of_first_random_node])
                tmpnodes = [n for n in G.neighbors(list_nodes[index_of_first_random_node])]
                for tmpnode in tmpnodes:
                    sampled_graph_edges.append([list_nodes[index_of_first_random_node], tmpnode])

        self.G1.add_edges_from(sampled_graph_edges)
        return self.G1


