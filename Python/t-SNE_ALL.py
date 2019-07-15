#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy
from tSNE_Code import calc
numpy.set_printoptions(threshold=numpy.inf)

# ans = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000)
n_iter_list = [500, 700, 1000, 1500, 2000, 3500, 5000]
angle_list = [0.8, 0.6, 0.4, 0.2]
method_list = ['exact', 'barnes_hut']#
# ans =TSNE(metric='cosine',method='exact',angle=0.2, n_iter=2000, n_components=2, n_iter_without_progress= 50)
with open(r'E:\\暑期任务\\Python\\data\\oregonf_edges_vector.txt') as f:
    a = -1
    y_list = []
    while True:
        lines = f.readline().replace('\n', '')
        a += 1
        if not lines:
            break
            pass
        if a == 0:
            continue
        x_list = lines.split(' ')
        y_list.append(x_list[0])
        x_list.remove(x_list[0])
        if a == 1:
            x_array = numpy.array(x_list)
        else:
            b_array = numpy.array(x_list)
            x_array = numpy.vstack((x_array, b_array))
        print("reading =======================", a)
    for i in n_iter_list:
        for a in angle_list:
            for m in method_list:
                if i == 500 & i == 700 & i == 1000:
                    break
                calc(x_array, i, a, m, y_list)

