import json
import numpy as np

with open("sampling_kde_kl.json") as f:
    txt_list = json.load(f)
    ans_list = []
    a = 0
    temp2_dict = {}
    for txt in txt_list:
        a += 1
        key_list = list(txt.keys())
        rate = (key_list[1].split('-'))[1]
        temp_dict = {rate: {"node": txt[key_list[1]]["node"],
                            "edge": txt[key_list[1]]["edge"],
                            "kde": txt[key_list[1]]["kde"],
                            "kl": txt[key_list[1]]["kl"]}}
        temp2_dict.update(temp_dict)
        if a == 8:
            a = 0
            ans_list.append({txt[key_list[0]]: temp2_dict})
        pass
    pass
    print(ans_list)
    json_str = json.dumps(ans_list)
    f_json = open("sampling_kde_kl_gai.json", 'w+')
    f_json.write(json_str)
