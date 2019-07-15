from sklearn.neighbors.kde import KernelDensity
import numpy as np
import csv
import os

# X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
# y = kde.score_samples(X)
# print(y)

for i in range(1,9):
    rate = i * 5
    file_name ='oregonf_sampling_tsne_RW_' + str(rate) + '_id_x_y.csv'
    f_path = os.path.join(r'E:\暑期任务\Python\data\sampling_t_SNE\RW\\' + file_name)

    with open(f_path) as f:
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

        kde = KernelDensity(kernel='exponential', bandwidth=0.2).fit(x_array)
        kde_list = np.exp(kde.score_samples(x_array))
        filename = 'oregonf_TSNE_RW_' + str(rate) + '_id_x_y_kde' + '.csv'
        file = os.path.join(r'E:\暑期任务\Python\data\kde\RW\\', filename )
        f_kde = open(file, 'w+', newline='')
        csv_write = csv.writer(f_kde, dialect='excel')
        a = 0
        csv_write.writerow(["id", "x", "y", "kde"])
        for i in kde_list:
            a += 1
            x = [y_id_list[a-1], y_list[a-1][0], y_list[a-1][1],i]
            print("write line ===============", a)
            csv_write.writerow(x)
        print("write over =========== " + str(rate))

