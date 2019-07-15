import csv

"""
    general experiment data to gephi format
    The header of the edgelist must be Source, Target
    
"""

# load node data
f = open('Datasets/CLASS1881/nodes.csv', 'r')
reader = csv.reader(f)
class1881_with_outlier_label = []
for item in reader:
    label = 0
    if reader.line_num == 1:
        continue
    if item[4] == '1' and item[5] == '0' and item[6] == '0':
        label = 1
    elif item[4] == '0' and item[5] == '1' and item[6] == '0':  # only Repeater
        label = 2
    elif item[4] == '0' and item[5] == '0' and item[6] == '1':  # only Sweetsgiver
        label = 3
    else:
        label = 0
    data = [int(item[0]), (item[1]), label]

    class1881_with_outlier_label.append(data)
f.close()
print (class1881_with_outlier_label)

# Write nodefile to gephi format
fw = open('Datasets/CLASS1881/nodes_output.csv', 'wb')
writer = csv.writer(fw)
writer.writerow(['ID', 'Label', 'Class'])
for row in class1881_with_outlier_label:
    writer.writerow(row)

# deal with edges file
f = open('Datasets/CLASS1881/edges.csv', 'r')
reader = csv.reader(f)
edges = []
for item in reader:
    if reader.line_num == 1:
        continue
    edges.append([int(item[0]), int(item[1])])
f.close()
print(edges)

# Write edgefile to gephi format
fw = open('Datasets/CLASS1881/edges_output.csv', 'wb')
writer = csv.writer(fw)
for row in edges:
    writer.writerow(row)
