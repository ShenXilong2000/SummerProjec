import json

f_csv = open(r"samling_kl.csv")
kl_list = []
ans_list = []
while True:
    lines = f_csv.readline().replace('\n', '')
    if not lines:
        break
    line = lines.split(',')
    kl_list.append(line[2])
pass

with open(r"sampling_kde.json") as f:
    txt_list = json.load(f)
    a = -1
    for txt in txt_list:
        a += 1
        key_list = list(txt.keys())
        temp_dict = {key_list[0]: txt[key_list[0]],
                     key_list[1]: {"node": txt[key_list[1]]["node"],
                                   "edge": txt[key_list[1]]["edge"],
                                   "kde": txt[key_list[1]]["kde"],
                                   "kl": kl_list[a]}}
        ans_list.append(temp_dict)
    pass

    json_str = json.dumps(ans_list)
    f_json = open("sampling_kde_kl.json", "w+")
    f_json.write(json_str)

