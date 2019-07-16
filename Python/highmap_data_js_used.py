import csv
datas = []
with open(r"samplingName_rate_db_highmapData_gai.csv") as f:
    # f_csv = open("samplingName_rate_db_highmapData_gai.csv", 'w+', newline='')
    # csv_write = csv.writer(f_csv, dialect='excel')
    # a = 0
    while True:
        lines = f.readline().replace('\n', '')
        if not lines:
            break
        txt_list = lines.split(',')
        if int(txt_list[1]) == 5:
            datas.append([int(txt_list[4]), int(txt_list[2]), float(txt_list[3])])
    print(datas)
    #     x = 0
    #     a += 1
    #     if a == 8:
    #         a = 0
    #         x += 1
    #     csv_write.writerow([txt_list[0], txt_list[1], txt_list[2], txt_list[3], x])