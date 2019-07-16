from sklearn.neighbors.kde import KernelDensity
import numpy as np
import csv
import os

# X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
# y = kde.score_samples(X)
# print(y)


with open(r'E:\暑期任务\Python\data\oregonf_TSNE_id_x_y_5000.csv') as f:
    a = -1
    x_list = []
    y_list = []
    y_id_list = []
    while True:
        lines = f.readline().replace('\n', '')
        a += 1
        if not lines:
            break
        if a == 0:
            continue
        x_list = lines.split(',')
        y_list.append(x_list)
        y_id_list.append(x_list[0])
        x_list.remove(x_list[0])
        if a == 1:
            x_array = np.array(x_list)
        else:
            temp_array = np.array(x_list)
            x_array = np.vstack((x_array, temp_array))
        print("read line ================", a)
    # kernel_list = ['gaussian', 'tophat', 'epanechnikov', 'exponential', 'linear', 'cosine']
    # for k in kernel_list:
    kde = KernelDensity(kernel='exponential', bandwidth=0.2).fit(x_array)
    kde_list = np.exp(kde.score_samples(x_array))
    filename = 'oregonf_TSNE_5000' + '_id_x_y_kde' + '.csv'
    file = os.path.join( 'E:\暑期任务\Python\data\kde', filename )
    f_kde = open(file, 'w+', newline='')
    csv_write = csv.writer(f_kde, dialect='excel')
    a = 0
    csv_write.writerow(["id", "x", "y", "kde"])
    for i in kde_list:
        a += 1
        print("write line ===============", a)
        x = [y_id_list[a-1], y_list[a-1][0], y_list[a-1][1], i]
        csv_write.writerow(x)
    print("write over")
