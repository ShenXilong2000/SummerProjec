import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

G = nx.DiGraph()
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,5)
G.add_edge(2,1)
G.add_edge(2,3)
G.add_edge(3,1)
G.add_edge(3,4)
G.add_edge(4,1)
G.add_edge(4,2)
G.add_edge(5,1)
G.add_edge(5,4)

a = G.in_degree(2)
b = G.out_degree(2)
h = list(G.successors(2))
i = list(G.predecessors(2))
j = list(G.neighbors(2))
f = list(set(h).intersection(set(i)))
z = len(f)
y = a + b - z

c = sorted(list(set(h+i)))
d = len(c)
e = a + b - d

print(a, b, c, d, e, h, i, j, z, y)

nx.draw(G, with_labels=True)
plt.show()