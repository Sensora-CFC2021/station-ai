import json


JSON_CORN_FILE_PATH = "/Users/itgel/PycharmProjects/LiquidPrep/Sensora/Crop/corn.json"
JSON_SOYABEAN_FILE_PATH = "/Users/itgel/PycharmProjects/LiquidPrep/Sensora/Crop/soybeans"

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
        return "Crop not selected."
