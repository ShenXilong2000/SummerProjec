import random
import networkx as nx

class RandomEdge():

    def __init__(self):
        self.G1 = nx.Graph()

    def randomedge(self, G, size):
        list_edges = list(G.edges())

        upper_bound_nr_nodes_to_sample = size

        nr_edges = len(list_edges)
        sampled_graph_edges = []

        while (len(sampled_graph_edges) < upper_bound_nr_nodes_to_sample):
            index_of_first_random_edges = random.randint(0, nr_edges - 1)
            sampled_graph_edges.append(list_edges[index_of_first_random_edges])

        self.G1.add_edges_from(sampled_graph_edges)
        return self.G1

