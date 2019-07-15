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
    for i in range(1, 9):
        rate = i * 5
        file_name = "oregonf_sampling_TIES_" + str(rate) + "_Source_Target.csv"     #read file name
        write_name = "oregonf_sampling_tsne_TIES_" + str(rate) + "_id_x_y.csv"      #write file name
        file = os.path.join(r'E:\暑期任务\Python\data\sampling\TIES\\', file_name)    #read file path
        write_file = os.path.join(r'E:\暑期任务\Python\data\sampling_t_SNE\TIES\\', write_name)      #write file path
        f_id = open(file)
        f_write = open(write_file, "w+", newline='')
        csv_wirte = csv.writer(f_write, dialect='excel')
        csv_wirte.writerow(["id", "x", "y"])
        id_list = []
        while True:
            lines = f_id.readline().replace('\n', '')
            if not lines:
                break
            x = lines.split(',')
            id_list.append(x[0])
        print(len(id_list))
        for id_ in id_list:
            for j in range(len(x_dict_tsne)):
                if round(float(x_dict_tsne[j]["id"])) == round(float(id_)):
                    temp_list = [round(float(id_)), x_dict_tsne[j]["x"], x_dict_tsne[j]["y"]]
                    csv_wirte.writerow(temp_list)
                    break
