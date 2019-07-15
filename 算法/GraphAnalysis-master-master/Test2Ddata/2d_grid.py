import copy

import matplotlib.pyplot as plt
import random
import numpy as np

# create data
x1 = [random.randrange(100) for i1 in range(500)]
y1 = [random.randrange(100) for j1 in range(500)]
x2 = [random.randrange(50) for i2 in range(20)]
y2 = [random.randrange(50) for j2 in range(20)]
x3 = [random.randrange(30) for i3 in range(30)]
y3 = [random.randrange(30) for j3 in range(30)]
x = x1 + x2 + x3
y = y1 + y2 + y3

dots = list(zip(x, y))

fig = plt.figure(figsize=(100, 100), dpi=100)
ax1 = fig.add_subplot(111)

# set title
ax1.set_title('Scatter Plot')

# set lebel
plt.xlabel('X')
plt.ylabel('Y')

# draw grid
for i in [i*10 for i in range(10)]:
    plt.plot([0,100],[i,i],color='#cccccc')

for i in [i*10 for i in range(10)]:
    plt.plot([i,i],[0,100],color='#cccccc')

# draw scatter
ax1.scatter(x,y,s=2)
plt.xlim(0, 100)
plt.ylim(0, 100)

def matrix2dict(matrix):
    pass


num_doc = {}
for dot in dots:
    default = num_doc.get((dot[0]//10, dot[1]//10), 0)
    num_doc.update({(dot[0]//10, dot[1]//10): default+1})
num_doc = dict(sorted(num_doc.items(), key=lambda d:d[0]))


list_doc = {}
num_uniq_doc = {}

for dot in dots:
    default_list = list_doc.get((dot[0] // 10, dot[1] // 10), [])
    default_list.append(dot)
    list_doc.update({(dot[0] // 10, dot[1] // 10): default_list})
list_doc = dict(sorted(list_doc.items(), key=lambda d:d[0]))

for lt in list_doc:
    default = list_doc.get(lt, [])
    num_uniq_doc.setdefault(lt, len(list(set(default))))
num_uniq_doc = dict(sorted(num_uniq_doc.items(), key=lambda d:d[0]))

for k, v in num_doc.items():
    print("1==>", k, v)
    print("2==>", k, num_uniq_doc.get(k))

value_doc = {}
for i in num_doc.values():
    default_value = value_doc.get(i, 0)
    value_doc.update({i: default_value + 1})
value_doc = dict(sorted(value_doc.items(), key=lambda d:d[0]))

value_uniq_doc = {}
for i in num_uniq_doc.values():
    default_value = value_uniq_doc.get(i, 0)
    value_uniq_doc.update({i: default_value + 1})
value_uniq_doc = dict(sorted(value_uniq_doc.items(), key=lambda d:d[0]))

unequal_zero_num = len(num_doc)
max_dots = max(num_uniq_doc.values())
print(unequal_zero_num, max_dots)
interval = unequal_zero_num // max_dots
print("interval:", interval)

updated_num_uniq_doc = copy.copy(num_uniq_doc)
updated_value_uniq_doc = copy.copy(value_uniq_doc)

print([(k, v) for k, v in value_doc.items()])
print([(k, v) for k, v in num_uniq_doc.items()])
# print([(k, v) for k, v in dict(sorted(num_uniq_doc.items(), key=lambda d:d[1])).items()])


temp_sum = 0
index = 1
for k, v in value_doc.items():
    filter_dots = filter(lambda d: d[1] == k, num_doc)
    for d in filter_dots:
        updated_num_uniq_doc.update({d: index})
    temp_sum += v
    if temp_sum > interval:
        temp_sum = 0
        index += 1


# print([(k, v) for k, v in updated_value_uniq_doc.items()])
# print([(k, v) for k, v in dict(sorted(updated_num_uniq_doc.items(), key=lambda d:d[1])).items()])

updated_value_uniq_doc = {}
for i in updated_num_uniq_doc.values():
    default_value = updated_value_uniq_doc.get(i, 0)
    updated_value_uniq_doc.update({i: default_value + 1})
updated_value_uniq_doc = dict(sorted(updated_value_uniq_doc.items(), key=lambda d:d[0]))

print([(k, v) for k, v in updated_value_uniq_doc.items()])
print([(k, v) for k, v in updated_num_uniq_doc.items()])
# set figure
#plt.show()



# a = [1,1,1,2,3]
# b = list(set(a))
# print(len(b))

