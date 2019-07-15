import numpy
import GraphClustering.Graph
import GraphClustering.MarkovClustering
from GraphRank.PageRank.utils import parse, print_results
from GraphRank.PageRank.pagerank import PageRank
import GraphSampling.modify_sample
import matplotlib.pyplot as plt
import operator
import networkx as nx
import csv

'''
    pagerank
'''
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
print(sorted_r)
sort_dict = {}
for i in sorted_r:
    sort_dict[i[0]] = i[1]
print(sort_dict)


'''
    graph cluster
'''
# load data
f = open("../Data/relationship.csv", "r")

grafo = GraphClustering.Graph.Graph()
for line in f:
    edges = line.strip().split(',')
    grafo.addNode(edges[0], edges[0])
    grafo.addNode(edges[1], edges[1])
    grafo.addEdge(edges[0], edges[1])

print("Graph adjacency list representation: \n",grafo)

matrix, mapBackToKeys = grafo.getGraphMatrix()
numpymat = numpy.array(matrix)
print("Graph matrix representation: \n",numpymat)
print("\nMapping matrix indexes to keys: ", mapBackToKeys)

alg = GraphClustering.MarkovClustering.MarkovClustering(matrix,e=2,r=2)
clusters = alg.computeClusters(T=40)

print("\nClusters after MCL algorithm: ")
num_count_cluster = []
total_clusters = len(clusters)
for cluster in clusters:
    print ([mapBackToKeys[x] for x in cluster])
    num_count_cluster.append(len(cluster))

print(num_count_cluster)

'''
     prepare sampling
'''
# set sampling rate
total = len(G.nodes())
rate = 0.7
sample_rate = int(total * rate)

cluster_score = []
for cluster in clusters:
    cluster_tmp_score = {}
    for x in cluster:
        if mapBackToKeys[x] in sort_dict:
            cluster_tmp_score[mapBackToKeys[x]]=sort_dict[mapBackToKeys[x]]
    cluster_score.append(cluster_tmp_score)
# print(cluster_score)
count_thresold = 4

which_need_sample = []
which_do_not_need_sample = []
for i in cluster_score:
    if len(i) > count_thresold:
        which_need_sample.append(sorted(i.keys(), reverse = True))
    else:
        which_do_not_need_sample.append(sorted(i.keys(), reverse = True))

print('----')
print(which_need_sample)
print(which_do_not_need_sample)

sample_object = GraphSampling.modify_sample.MHRW()
sample1 = sample_object.mhrw(G, sample_rate, which_need_sample)
print(sample1)

# show graph
nx.draw(sample1, with_labels=True)
plt.show()
plt.close()