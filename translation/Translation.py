import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

JSON_SOURCE_FILE_PATH = dir_path + "/source.json"
JSON_ADVICE_FILE_PATH = dir_path + "/advice.json"

with open(JSON_SOURCE_FILE_PATH) as f:
    source_data = json.load(f)

with open(JSON_ADVICE_FILE_PATH) as f:
    advice_data = json.load(f)


def translated_advice(language):
    # noinspection PyBroadException
    try:
        return source_data[language]
    except Exception:
        return "Language not supported."


def translated_final_advice(language, water_advice):
    advice_in_chosen_lan = advice_data[language]
    print(advice_in_chosen_lan["CROP_NAME"], water_advice.crop_name)
    print(advice_in_chosen_lan["STAGE"], water_advice.stage)
    print(advice_in_chosen_lan["RECOMMENDED_WATER_USE"], water_advice.water_recommended, advice_in_chosen_lan["UNIT"])
    print(advice_in_chosen_lan["IRRIGATION ADVICE"], water_advice.watering_decision)
