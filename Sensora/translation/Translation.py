import json


JSON_SOURCE_FILE_PATH = "/Users/itgel/PycharmProjects/LiquidPrep/Sensora/Translation/source.json"

with open(JSON_SOURCE_FILE_PATH) as f:
    source_data = json.load(f)

def translated_advice(language):
    # noinspection PyBroadException
    try:
        return source_data[language]
    except Exception:
        return "Language not supported."
