import GraphSampling
import networkx as nx
import matplotlib.pyplot as plt
import csv

# load graph to networkx
f = open(r'E:\暑期任务\Python\data\oregonf.csv', "r")
reader1 = csv.reader(f)
edges = []
for item in reader1:
    edges.append([float(item[0]), float(item[1])])
f.close()
G = nx.Graph()
G.add_edges_from(edges)


# set sampling rate
total = len(G.nodes())
rate = 0.5
sample_rate = int(total * rate)

RN_object = GraphSampling.RandomNode()
RN_sample = RN_object.randomnode(G, sample_rate)  # graph, number of nodes to sample

# convert to node list
nodes = []
for node in RN_sample.nodes():
    nodes.append([node, 3])

# convert to edge list
edges = []
for edge in RN_sample.edges():
    edges.append(edge)


# # save as csv


fw = open(r"E:\\暑期任务\\Python\\oregonf_sampling_node.csv", 'w+', newline='')
writer = csv.writer(fw, dialect='excel')
writer.writerow(["ID", "Class"])
for row in nodes:
    writer.writerow(row)

fw = open(r"E:\\暑期任务\\Python\\oregonf_sampling_edge.csv", 'w+', newline='')
writer = csv.writer(fw, dialect='excel')
writer.writerow(["Source", "Target"])
for row in edges:
    writer.writerow(row)