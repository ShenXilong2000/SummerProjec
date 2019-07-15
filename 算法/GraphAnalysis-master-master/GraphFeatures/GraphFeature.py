import networkx as nx
import matplotlib.pyplot as plt
import csv

G0 = nx.Graph()

# add attribute nodes
# set parameter
filename = 'Data/nodes_output.csv'

# load graph data
f = open(filename, "r")
reader1 = csv.reader(f)
for item in reader1:
    G0.add_node(int(item[0]), name = item[1], type = item[2])
f.close()

print(G0.number_of_nodes())

'''
nodes feature example (high degree example)
'''

G = G0.copy()
# person1's friends
for node in G.nodes():
    if node == 1:
        continue
    else:
        G.add_edge(1, node)
    if node == 25:
        break

# person2's friends
for node in G.nodes():
    if node < 25:
        continue
    else:
        G.add_edge(2, node)
    if node == 29:
        break

# person3's friends
for node in G.nodes():
    if node < 29:
        continue
    else:
        G.add_edge(3, node)
    if node == 32:
        break

pos = nx.spring_layout(G)

plt.subplot(321)
plt.title('nodes feature')
nx.draw(G,pos)
node_labels = nx.get_node_attributes(G, 'name')
nx.draw_networkx_labels(G, pos, labels = node_labels)

'''
edges feature example (high degree example)
'''
G1 = G.copy()

# add 6 friends to person1's friends circle
G1.add_edge(2,3)
G1.add_edge(3,4)
G1.add_edge(3,5)
G1.add_edge(7,8)
G1.add_edge(7,10)
G1.add_edge(11,15)

plt.subplot(322)
plt.title('edges feature')
nx.draw(G1,pos)
node_labels = nx.get_node_attributes(G1, 'name')
nx.draw_networkx_labels(G1, pos, labels = node_labels)

'''
near clique example 
'''
G2 = G0.copy()
for node1 in G.nodes():
    for node2 in G.nodes():
        if node1 <= node2:
            continue
        else:
            G2.add_edge(node1, node2)
        if node1 >= 20:
            break
    if node1 >= 20:
        break

plt.subplot(323)
plt.title('near-clique')
nx.draw(G2,pos)
node_labels = nx.get_node_attributes(G2, 'name')
nx.draw_networkx_labels(G2, pos, labels = node_labels)

'''
Heavy vicinity example 
'''
G3 = nx.Graph()
G3.add_weighted_edges_from([(1,2,2.0),(1,3,7.5),(2,3,1.0),(2,4,6.5),(1,4,1.0),(2,5,1.0),(3,4,4.0),(4,5,1.0)])
weights = []
for u,v,w in G3.edges.data('weight'):
    weights.append(w)
print(weights)

plt.subplot(324)
plt.title('heavy vicinity')
nx.draw(G3,pos, width = weights)
# weights = [w[2]['weight']*5 for w in G3.edges(data=True)]
node_labels = nx.get_node_attributes(G3, 'name')
nx.draw_networkx_labels(G3, pos, with_labels=True)

'''
Dominant heavy links 
'''


# show plots
plt.show()