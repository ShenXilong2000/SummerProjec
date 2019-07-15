import networkx as nx
import csv
import pandas as pd

# set parameter
original_path = 'Data/email-Eu-core.csv'

# load graph data
f = open(original_path, 'r')
reader = csv.reader(f)
edges = []
for item in reader:
    edges.append([int(item[0]), int(item[1])])
f.close()

G = nx.DiGraph()
G.add_edges_from(edges)
# print(G.edges())

# calculate dgree
graph_info = []
node_ID = []

indegree = []
outdegree = []
bidegree = []
sumdegree = []

for node in G.nodes():

    node_ID.append(str(node))

    in_degree = G.in_degree(node)
    out_degree = G.out_degree(node)

    indegree.append(in_degree)
    outdegree.append(out_degree)

    in_nodes = list(G.successors(node))
    out_nodes = list(G.predecessors(node))

    bi_num = len(list(set(in_nodes).intersection(set(out_nodes))))
    merge_num = in_degree + out_degree - bi_num

    sumdegree.append(merge_num)
    bidegree.append(bi_num)
    graph_info.append([str(node), in_degree, out_degree, bi_num, merge_num])
print(graph_info)

# save as csv
title = ['ID', 'Indegree', 'Outdegree', 'Bidegree', 'Sumdegree']
test = pd.DataFrame(columns=title, data=graph_info)
test.to_csv('Data/email-eu-core-result.csv')
print('finish')
