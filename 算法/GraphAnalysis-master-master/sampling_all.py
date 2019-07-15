import GraphSampling
import networkx as nx
import csv
import os

# load graph to networkx
f = open(r'E:\暑期任务\Python\data\oregonf.txt', "r")
# reader1 = csv.reader(f)
edges = []
# for item in reader1:
#     edges.append([float(item[0]), float(item[1])])
while True:
    lines = f.readline().replace('\n', '')
    if not lines:
        break
    edge = lines.split('\t')
    edges.append([edge[0], edge[1]])
f.close()
G = nx.Graph()
G.add_edges_from(edges)


# set sampling rate
total = len(G.nodes())
rate_list = []
for i in range(1, 9):
    rate_list.append(round((0.05*i), 2))


for rate in rate_list:
    sample_rate = int(total * rate)

    # make an object and call function RW
    RW_object = GraphSampling.SRW_RWF_ISRW()
    RW_sample = RW_object.random_walk_sampling_simple(G, sample_rate)  # graph, number of nodes to sample

    # make an object and call function RWF
    # BFS_object = GraphSampling.BFS()
    # BFS_sample = BFS_object.bfs(G, sample_rate)  # graph, number of nodes to sample

    # convert to node list
    nodes = []
    for node in RW_sample.nodes():   #===========================
        nodes.append([node, 3])

    # convert to edge list
    edges = []
    for edge in RW_sample.edges():
        edges.append(edge)

    # # save as csv
    fileName = 'oregonf_sampling_RW_' + str(round(rate*100)) + "_Source_Target.csv"
    file = os.path.join(r"E:\暑期任务\Python\data\sampling\RW" + fileName)

    fw = open(file, 'w+', newline='')
    writer = csv.writer(fw, dialect='excel')
    for row in nodes:`
        x = [round(float(row[0]))]
        writer.writerow(x)

    print("now sampling  ================= " + str(round(rate*100)))
print("write over")
