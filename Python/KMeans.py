import numpy as np  # 数据结构
from sklearn.cluster import KMeans  # 密度聚类
from sklearn import metrics   # 评估模型
import matplotlib.pyplot as plt  # 可视化绘图
import json

with open(r"E:\暑期任务\Python\data\oregonf_TSNE_5000_id_x_y_kde.csv") as f:
    lines = f.readline()
    datas = []
    ids = []
    while True:
        lines = f.readline().replace('\n','')
        if not lines:
            break
        txt = lines.split(',')
        data = [round(float(txt[1]), 30), round(float(txt[2]),30)]
        datas.append(data)
        ids.append([int(txt[0]), round(float(txt[3]), 30)])
    pass
    X = np.array(datas)
    # print(X)
    for j in range(10, 50):
        km = KMeans(n_clusters=j).fit(X)
        labels = km.labels_
        for x in range(j):
            x_list = X[labels == x]
            # plt.scatter(x_list[:, 0], x_list[:, 1], c=color_list[x], marker='.')
            plt.plot( x_list[:, 0], x_list[:, 1], "o", markersize=1)
        file_name = "aaa" + str(j) +".png"
        plt.savefig(file_name)


        # ans_dict = {}
        # for i in range(n_clusters_):
        #     temp_dict = {}
        #     for lb in range(len(labels)):
        #         if labels[lb] == i:
        #             ans = {int(ids[lb][0]): {"x": datas[lb][0], "y": datas[lb][1], "kde": ids[lb][1]}, }
        #             temp_dict.update(ans)
        #         pass
        #     pass
        #     ans_dict.update({i: temp_dict})

    # ans_dict = {}
    # for i in range(len(labels)):
    #     ans = {int(ids[i]): {"x": datas[i][0], "y": datas[i][1], "dbscan": int(labels[i])}}
    #     ans_dict.update(ans)

    # print(ans_dict)
    # f_json = open("dbscan_id_x_y_cbj.json", "w+")
    # json_str = json.dumps(ans_dict)
    # f_json.write(json_str)

    # # print('每个样本的簇标号:')
    # # print(labels)
    #
    # raito = len(labels[labels[:] == -1]) / len(labels)  #计算噪声点个数占总数的比例
    # # print('噪声比:', format(raito, '.2%'))
    #
    # n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)  # 获取分簇的数目
    #
    # print('分簇的数目: %d' % n_clusters_)
    # print("轮廓系数: %0.3f" % metrics.silhouette_score(X, labels)) #轮廓系数评价聚类的好坏
    #
    # for i in range(n_clusters_):
    #     # print('簇 ', i, '的所有样本:')
    #     one_cluster = X[labels == i]
    #     # print(one_cluster)
    #     plt.plot(one_cluster[:, 0], one_cluster[:, 1], 	"o", markersize=1)
    #
    # file_name = str(eps)+'___' + str(n_clusters_) +".png"
    # plt.savefig(file_name)
    # plt.show()