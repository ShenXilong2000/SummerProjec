import GraphSampling
import networkx as nx
import matplotlib.pyplot as plt
import csv

# load graph to networkx
f = open("Data/relationship.csv", "r")
reader1 = csv.reader(f)
edges = []
for item in reader1:
    edges.append([int(item[0]), int(item[1])])
f.close()
G = nx.Graph()
G.add_edges_from(edges)


# set sampling rate
total = len(G.nodes())
rate = 0.5
sample_rate = int(total * rate)

# run sample algorithm
'''
    sample1 - random_node   ===
    sample2 - random_edge      ====  
    sample3 - bfs             ====
    sample4 - snowball     //
    sample5 - forestfire   //
    sample6 - random_walk_sampling_simple     
    sample7 - random_walk_sampling_with_fly_back
    sample8 - random_walk_induced_graph_sampling
    sample9 - mhrw
    sample10 - induced_mhrw     ?
    sample11 - ties    ======
    sample12 - rj       ====
    
'''

# make an object and call function RN
# RN_object = GraphSampling.RandomNode()
# RN_sample = RN_object.randomnode(G, sample_rate)  # graph, number of nodes to sample

# make an object and call function RE
# RE_object = GraphSampling.RandomEdge()
# RE_sample = RE_object.randomedge(G, sample_rate)  # graph, number of nodes to sample

# make an object and call function BFS
# BFS_object = GraphSampling.BFS()
# BFS_sample = BFS_object.bfs(G, sample_rate)  # graph, number of nodes to sample

# make an object and call function SB
# SB_object = GraphSampling.Snowball()
# SB_sample = SB_object.snowball(G, sample_rate, 6)  # graph, number of nodes to sample

# make an object and call function FF
# FF_object = GraphSampling.ForestFire()
# FF_sample = FF_object.forestfire(G, sample_rate)  # graph, number of nodes to sample

# make an object and call function RW
# RW_object = GraphSampling.SRW_RWF_ISRW()
# RW_sample = RW_object.random_walk_sampling_simple(G, sample_rate)  # graph, number of nodes to sample

# make an object and call function RWF
# RWF_object = GraphSampling.SRW_RWF_ISRW()
# RWF_sample = RWF_object.random_walk_sampling_with_fly_back(G, sample_rate, 0.2)  # graph, number of nodes to sample

# make an object and call function ISRW
# ISRW_object = GraphSampling.SRW_RWF_ISRW()
# ISRW_sample = ISRW_object.random_walk_induced_graph_sampling(G, sample_rate)  # graph, number of nodes to sample

# make an object and call function MHRW
# MHRW_object = GraphSampling.MHRW()
# MHRW_sample = MHRW_object.mhrw(G, sample_rate)  # graph, number of n

# make an object and call function MHRW
# ISMHRW_object = GraphSampling.MHRW()
# ISMHRW_sample = ISMHRW_object.induced_mhrw(G, sample_rate)  # graph, number of n

# make an object and call function TIES
# TIES_object = GraphSampling.TIES()
# TIES_sample = TIES_object.ties(G, sample_rate)  # graph, number of n


# make an object and call function RJ
RJ_object = GraphSampling.RJ()
RJ_sample = RJ_object.rj(G, sample_rate)  # graph, number of n
# info
# print(FF_sample.nodes())
# print("Number of nodes sampled=", len(FF_sample.nodes()))
# print("Number of edges sampled=", len(FF_sample.edges()))
# print("degree", nx.degree_histogram(FF_sample))
# print("cluster",  nx.average_clustering(FF_sample))
nx.draw(RJ_sample, with_labels=True)
plt.show()

# convert to node list
# nodes = []
# for node in FF_sample.nodes():
#     nodes.append([node, 3])
# print nodes

# convert to edge list
# edges = []
# for edge in RW_sample.edges():
#     edges.append(edge)


# # save as csv
# fw = open(nodefile_path, 'wb')
# writer = csv.writer(fw)
# writer.writerow(['ID', 'Class'])
# for row in nodes:
#     writer.writerow(row)
#
# fw = open(edgefile_path, 'wb')
# writer = csv.writer(fw)
# writer.writerow(['Source', 'Target'])
# for row in edges:
#     writer.writerow(row)