import networkx as nx
import matplotlib.pyplot as plt


'''
    node anomaly
'''
# undirected
G1 = nx.Graph()

# person1's friends
for node in range(1,200):
    if node == 1:
        continue
    else:
        G1.add_edge(1, node)
    if node == 151:
        break

pos = nx.spring_layout(G1)

plt.title('undirected star')
nx.draw(G1,pos)
nx.draw_networkx_labels(G1, pos, with_labels=True)

# show plot
plt.show()