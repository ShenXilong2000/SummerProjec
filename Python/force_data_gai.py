import json
import numpy as np

with open(r'E:\暑期任务\html\data\force_data.json') as f:
    ans_dict = {}
    txt_list = json.load(f)
    for txt in txt_list:
        ans_dict.update({txt["id"]: {"x": txt["x"], "y": txt["y"]}})
        # ans_dict = np.vstack(ans_dict, temp_dict)
file = open("force_data_gai.json", "w+")
json_str = json.dumps(ans_dict)
file.write(json_str)
