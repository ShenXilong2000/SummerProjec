import numpy as np
from scipy import stats
import scipy
import json
import csv


def KL_divergence(p, q):
    return scipy.stats.entropy(p, q)
def symmetricalKL(P, Q):
    return (KL_divergence(P, Q) + KL_divergence(Q, P)) / 2.00
def takefist(elem):
    return elem[0]


sampling_100 = []
flag = True
with open(r"E:\暑期任务\Python\data\kde\oregonf_TSNE_exponential_id_x_y_kde.csv") as f:
    while True:
        lines = f.readline().replace('\n', '')
        if not lines:
            break
        if flag == True:
            flag = False
            continue
        x_list = lines.split(',')
        sampling_100.append([int(x_list[0]), x_list[3]])
sampling_100.sort(key=takefist)
# for i in sampling_100:
#     ans_100_list.append(i[1])
ans = []
f_csv = open("samling_kl.csv", 'w+', newline='')
csv_write = csv.writer(f_csv, dialect='excel')
with open(r"E:\暑期任务\Python\sampling_kde.json") as f:
    txt_dict = json.load(f)
    # a = 0
    for txt in txt_dict:
        # a += 1
        # if a <=7 :
        #     continue
        x_list = []
        key_list = list(txt.keys())
        kde_list = txt[key_list[1]]["kde"]
        for i in range(len(kde_list)):
            x_list.append([txt[key_list[1]]['node'][i], kde_list[i]])
        ans_sampling_list = []
        ans_100_list = []
        x_list.sort(key=takefist)
        for i in x_list:
            ans_sampling_list.append(i[1])
            # ans_100_list.append(sampling_100[sampling_100.index(int(i[0]))][1])
            for j in sampling_100:
                if round(float(j[0])) == round(float(i[0])):
                    ans_100_list.append(round(float(j[1]), 30))
                    break
                if j[0] == sampling_100[len(sampling_100)-1][0]:
                    ans_sampling_list.remove(i[1])
        print(len(ans_sampling_list))
        print(len(ans_100_list))
        print(txt["name"]+","+key_list[1]+","+str(symmetricalKL(ans_100_list, ans_sampling_list)))
        ans.append([txt["name"], key_list[1], str(symmetricalKL(ans_100_list, ans_sampling_list))])
    for row in ans:
        csv_write.writerow(row)


# #自己编程实现
# kl= 0.0
# for i in range(10):
#     kl += px[i] * np.log(px[i]/py[i])
# print(k)

