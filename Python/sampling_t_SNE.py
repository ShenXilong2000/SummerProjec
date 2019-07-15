import os
import csv

with open(r'E:\暑期任务\Python\data\oregonf_TSNE_id_x_y_5000.csv') as f_tsne:
    x_dict_tsne = []
    a = -1
    while True:
        a += 1
        lines = f_tsne.readline().replace('\n', '')
        if a == 0:
            continue

        if not lines:
            break
        x_list = lines.split(',')
        x_dict_tsne.append({"id": x_list[0], "x": x_list[1], "y": x_list[2], })
    for i in range(1, 21):
        rate = i * 5
        file_name = "oregonf_sampling_" + str(rate) + "_Source_Target.csv"
        write_name = "oregonf_sampling_tsne_" + str(rate) + "_id_x_y.csv"
        file = os.path.join(r'E:\暑期任务\Python\data\sampling', file_name)
        write_file = os.path.join(r'E:\暑期任务\Python\data\sampling_t_SNE', write_name)
        f_id = open(file)
        f_write = open(write_file, "w+", newline='')
        csv_wirte = csv.writer(f_write, dialect='excel')
        csv_wirte.writerow(["id", "x", "y"])
        flag = True
        id_list = []
        while True:
            lines = f_id.readline().replace('\n', '')
            if not lines:
                break
            if flag:
                flag = False
                continue
            x = lines.split(',')
            if x[0] not in id_list:
                id_list.append(x[0])
        print(len(id_list))
        for id_ in id_list:
            for j in range(len(x_dict_tsne)):
                if round(float(x_dict_tsne[j]["id"])) == round(float(id_)):
                    temp_list = [round(float(id_)), x_dict_tsne[j]["x"], x_dict_tsne[j]["y"]]
                    csv_wirte.writerow(temp_list)
                    break

