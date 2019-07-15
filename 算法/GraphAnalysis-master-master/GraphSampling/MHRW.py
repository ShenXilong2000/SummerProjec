import random
import networkx as nx

class MHRW():
    def __init__(self):
        self.G1 = nx.Graph()

    def mhrw(self, complete_graph, nodes_to_sample):

        list_nodes = list(complete_graph.nodes())
        nr_nodes = len(complete_graph.nodes())
        upper_bound_nr_nodes_to_sample = nodes_to_sample
        index_of_first_random_node = random.randint(0, nr_nodes-1)
        sampled_graph = nx.Graph()

        sampled_graph.add_node(list_nodes[index_of_first_random_node])

        curr_node = index_of_first_random_node
        curr_degree = complete_graph.degree(list_nodes[index_of_first_random_node])
        while sampled_graph.number_of_nodes() != upper_bound_nr_nodes_to_sample:
            edges = [n for n in complete_graph.neighbors(curr_node)]
            index_of_edge = random.randint(0, len(edges) - 1)
            chosen_node = edges[index_of_edge]
            new_degree = complete_graph.degree(edges[index_of_edge])
            sampled_graph.add_node(chosen_node)
            sampled_graph.add_edge(curr_node, chosen_node)

            p = random.random()
            d = float(curr_degree)/float(new_degree)
            if p <= min(1.0, d):
                curr_node = chosen_node

        return sampled_graph

    def induced_mhrw(self, G, size):
        sampled_graph = self.mhrw(G, size)
        induced_graph = G.subgraph(sampled_graph.nodes())
        return induced_graph