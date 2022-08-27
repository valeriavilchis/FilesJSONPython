import os
import json

parent_dir_int = 'Input'
parent_dir_out = 'Output'
list_content_jsons = os.listdir(parent_dir_int)

for file_json in list_content_jsons:
    dir_file = parent_dir_int+"/"+file_json
    
    with open(dir_file) as content:
        data_json = json.load(content)
        data_order = data_json['order']
        
        for dict_treat in data_order:
            del dict_treat['debit_entity']
    
        json_output = json.dumps(data_json)
        file_output = parent_dir_out + file_json
        if not os.path.exists(parent_dir_out):
            os.makedirs(parent_dir_out)
        dir_json_output = parent_dir_out+"/"+file_json
        with open(dir_json_output,"w") as fo:
            json.dump(data_json, fo)