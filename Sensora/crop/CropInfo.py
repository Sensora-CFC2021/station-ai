import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
JSON_CORN_FILE_PATH = dir_path + "/corn.json"
JSON_SOYABEAN_FILE_PATH = dir_path + "/soybeans.json"


with open(JSON_CORN_FILE_PATH) as f:
    corn_data = json.load(f)

with open(JSON_SOYABEAN_FILE_PATH) as f:
    soyabean_data = json.load(f)


def general_crop_info(crop):
    if crop == "corn":
        return corn_data
    elif crop == "soyabean":
        return soyabean_data
    else:
        return "No crop info found."


# print(general_crop_info("corn")) # testing
