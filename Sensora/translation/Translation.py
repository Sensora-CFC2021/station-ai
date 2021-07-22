import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

JSON_SOURCE_FILE_PATH = dir_path+"/source.json"

with open(JSON_SOURCE_FILE_PATH) as f:
    source_data = json.load(f)

def translated_advice(language):
    # noinspection PyBroadException
    try:
        return source_data[language]
    except Exception:
        return "Language not supported."
