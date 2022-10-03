import json
import os
from resources.avrodict import AVRO_DICT

if __name__ == '__main__':
    for dict in AVRO_DICT['data']['patterns']:
        print(dict['replace'])

# path = os.path.join(os.getcwd(), "avrodict_reversed.json")

# avro_dict = {}

# with open(path, "r", encoding='utf-8') as file:
#     avro_dict = json.load(file)

# while True:
#     find = input("find: ")

#     if find == "XX":
#         break

#     replace = input("replace: ")
    
#     avro_dict["data"]["patterns"].append({
#         "find": find,
#         "replace": replace
#     })


#     with open(path, "w", encoding='utf-8') as file:
#         content = json.dumps(avro_dict, indent=4, ensure_ascii=False)
#         file.write(content)
