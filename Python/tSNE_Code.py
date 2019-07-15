#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy
import csv
import os
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
numpy.set_printoptions(threshold=numpy.inf)


def calc(x_array, i, a, m, y_list):
    ans =TSNE(metric='cosine', method=m, angle=a, n_iter=i, n_components=2)
    x_tsne = ans.fit_transform(x_array)
    fileName = "oregonf_TSNE_i_" + str(i) + "_a_" + str(a) + "_m_" + str(m) + "_id_x_y" + ".csv"
    file = os.path.join(r'E:\暑期任务', fileName)
    f = open(file, 'a', newline='')
    csv_write = csv.writer(f, dialect='excel')
    times = 0
    x = []
    y = []
    for i in x_tsne:
        csv_ans = [y_list[times], i[0], i[1]]
        times += 1
        print(fileName + "===============" + str(times))
        csv_write.writerow(csv_ans)
        x.append(i[0])
        y.append(i[1])
    print(fileName + "===============" + "write over")
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(x, y, c='k', marker='o')
    plt.legend('x1')
    plt.savefig(fileName + ".png")
