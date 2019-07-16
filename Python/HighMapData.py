import json
import csv

with open("sampling_kde_kl_gai.json") as f:
    txt_list = json.load(f)
    f_dbscan = open(r'data/dbscan_id_x_y.json')
    dbscan_dict = json.load(f_dbscan)

    f_csv = open("samplingName_rate_db_highmapData.csv", "w+", newline='')
    csv_write = csv.writer(f_csv, dialect='excel')


    for txt in txt_list:
        for name in txt:
            for rate in txt[name]:
                for db in dbscan_dict:
                    node_db_list = list(map(int, list(dbscan_dict[db].keys())))
                    sum_kde_sampling = 0
                    for i in range(len(txt[name][rate]["node"])):
                        if txt[name][rate]["node"][i] in node_db_list:
                            if i < len(txt[name][rate]["kde"]):
                                sum_kde_sampling += txt[name][rate]["kde"][i]
                    sum_all_kde_db = 0
                    for id in node_db_list:
                        sum_all_kde_db += dbscan_dict[db][str(id)]["kde"]
                    ans = abs(sum_all_kde_db - sum_kde_sampling)/sum_all_kde_db
                    # print(str(rate) + "=========="+ str(db) + "==========" + str(sum_kde_sampling))
                    # print("===============")
                    csv_write.writerow([name, rate, db, ans])
                    ans = 0