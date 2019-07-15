from GraphRank.PageRank.utils import parse, print_results
from GraphRank.PageRank.pagerank import PageRank
import networkx as nx
import csv
import matplotlib.pyplot as plt
import operator
import GraphSampling.modify_sample

# set parameter
filename = '../Datasets/CLASS1881/class1881.csv'
isDirected = True

# load graph data
f = open(filename, "r")
reader1 = csv.reader(f)
edges = []
for item in reader1:
    edges.append([int(item[0]), int(item[2])])
f.close()
if isDirected:
    G = nx.DiGraph()
    G.add_edges_from(edges)
else:
    G = nx.Graph()
    G.add_edges_from(edges)

# get pagerank score
graph = parse(filename, isDirected)
p = PageRank(graph, isDirected)
p.rank()
sorted_r = sorted(p.ranks.items(), key=operator.itemgetter(1), reverse=True)

# get sampling parameter
total = len(G.nodes())
rate = 0.5
sample_rate = int(total * rate)

top_nodes = int(0.2 * sample_rate)
bottom_nodes = int(0.1 * sample_rate)

# get init sample nodes
top_score = []
for i in range(top_nodes):
    top_score.append(int(sorted_r[i][0]))

bottom_score = []
for i in range(len(sorted_r) - 1, len(sorted_r) - bottom_nodes - 1, -1):
    bottom_score.append(int(sorted_r[i][0]))

# set two kind of sample_rate
top_rate = int(round(0.5 * sample_rate))
bottom_rate = int(round(0.5 * sample_rate))

# get high score sampling nodes
sample_object = GraphSampling.modify_sample.Snowball()
sample1 = sample_object.snowball(G, top_score, top_rate)
print(sample1)

# get low score sampling nodes
sample_object = GraphSampling.modify_sample.Snowball()
sample2 = sample_object.snowball(G, bottom_score, bottom_rate)
print(sample2)

# merge nodes and get induced graph
nodes = sample1 + sample2
print(nodes)
sample_object = GraphSampling.modify_sample.InducedGraph()
sample_graph = sample_object.induced_graph(G, nodes)

# show graph
nx.draw(sample_graph, with_labels=True)
plt.show()
plt.close()

# show info

