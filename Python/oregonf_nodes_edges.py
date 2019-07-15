import json

nodes = []
edges = []
with open(r"data\oregonf_nodes.csv") as f:

    while True:
        lines = f.readline().replace('\n', '')
        if not lines:
            break
        node_list = lines.split(',')
        nodes.append(node_list[1])

with open(r"data\oregonf.csv") as f:

    while True:
        lines = f.readline().replace('\n', '')
        if not lines:
            break
        edge_list = lines.split(',')
        edges.append([edge_list[0], edge_list[1]])


json_str = json.dumps({"nodes": nodes, "edges": edges})
f_json = open(r"data/oregonf_nodes_edges.json", 'w+')
f_json.write(json_str)
