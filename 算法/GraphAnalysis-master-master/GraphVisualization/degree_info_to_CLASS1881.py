import networkx as nx
import csv
import matplotlib.pyplot as plt
import matplotlib

# set parameter
original_path = '../Datasets/CLASS1881/edges_output.csv'

# load graph data
f = open(original_path, 'r')
reader = csv.reader(f)
edges = []
for item in reader:
    edges.append([int(item[0]), int(item[1])])
f.close()

G = nx.DiGraph()
G.add_edges_from(edges)
# print G.edges()

# calculate dgree
graph_info = []
node_ID = []
indegree = []
outdegree = []
bidegree = []
sumdegree = []
for node in G.nodes():
    node_ID.append(str(node))
    indegree.append(G.in_degree(node))
    outdegree.append(G.out_degree(node))

    in_nodes = list(G.successors(node))
    out_nodes = list(G.predecessors(node))

    bi_num = len(list(set(in_nodes).intersection(set(out_nodes))))
    merge_num = G.in_degree(node) + G.out_degree(node) - bi_num

    sumdegree.append(merge_num)
    bidegree.append(bi_num)
print(node_ID[indegree.index(max(indegree))], node_ID[outdegree.index(max(outdegree))], node_ID[sumdegree.index(max(sumdegree))])


# show the result fig
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

label_list = node_ID
num_list1 = indegree
num_list2 = outdegree
num_list3 = bidegree
num_list4 = sumdegree
x = range(len(num_list4))

rects1 = plt.bar(left=x, height=num_list1, width=0.2, alpha=0.8, color='#004b8a', label="in_degree")
rects2 = plt.bar(left=[i + 0.2 for i in x], height=num_list2, width=0.2, color='#fe8a84', label="out_degree")
rects3 = plt.bar(left=[i + 0.4 for i in x], height=num_list3, width=0.2, color='#b8d7d8', label="bi_degree")
rects4 = plt.bar(left=[i + 0.6 for i in x], height=num_list4, width=0.2, color='#cccccc', label="sum_degree")

plt.ylim(0, max(sumdegree))
plt.ylabel("count")

plt.xticks([index + 0.4/4 for index in x], label_list)
plt.xlabel("node")
plt.title("degree count")
plt.legend()

for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
for rect in rects3:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
for rect in rects4:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
plt.show()


