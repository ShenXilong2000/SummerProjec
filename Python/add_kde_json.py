import json
import numpy as np
from sklearn.neighbors.kde import KernelDensity

ans_list = []
x_y = []
flag = True
with open(r'E:\暑期任务\Python\data\oregonf_TSNE_id_x_y_5000.csv') as f_x_y:
    while True:
        lines = f_x_y.readline().replace('\n', '')
        if flag:
            flag = False
            continue
        if not lines:
            break
        x_y_list = lines.split(',')
        x_y.append([x_y_list[0], x_y_list[1], x_y_list[2]])
with open(r"E:\暑期任务\Python\data\json_sampling.json") as f:
    file_json = open("sampling_kde.json", "w+")
    txt_dict = json.load(f)
    for txt in txt_dict:
        key_list = list(txt.keys())
        print(key_list[1])
        nodes_list = txt[key_list[1]]["node"]
        a = 0
        for node in nodes_list:
            for i in range(len(x_y)):
                if round(float(x_y[i][0])) == round(float(node)):
                    a += 1
                    if a == 1:
                        nodes_array = np.array([x_y[i][1], x_y[i][2]])
                    else:
                        temp_array = np.array([x_y[i][1], x_y[i][2]])
                        nodes_array = np.vstack((nodes_array, temp_array))

        kde = KernelDensity(kernel='exponential', bandwidth=0.2).fit(nodes_array)
        kde_list = np.exp(kde.score_samples(nodes_array))
        x_array = {key_list[0]: txt[key_list[0]], key_list[1]: {"node": txt[key_list[1]]["node"], "edge": txt[key_list[1]]["edge"], "kde": kde_list.tolist()}}
        ans_list.append(x_array)
        # print(kde_list.tolist())
    # print(ans_list)
    json_str = json.dumps(ans_list)
    file_json.write(json_str)