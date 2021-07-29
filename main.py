from translation import Translation
from service import SoilMoistureService, WeatherDataService, WaterAdviceService
from crop import CropInfo
from models import SelectedCrop, Crop
from textToSpeech import Watson, SpeechAdvice
from playsound import playsound


def sensora(soil_moisture_percentage, language, crop_information, coordinates):
    """
    soil_moisture_percentage: number - integer/float,
    language: string - "en" / "mn"
    crop_information: tuple containing the crop type and its growth stage
    coordinates: tuple of latitude and longitude
    """

    # --------------------------- TRANSLATION VARIABLES ---------------------------
    variables = Translation.translated_advice(language)

    # --------------------------- SOIL MOISTURE, SOIL MOISTURE INDEX ---------------------------
    soil_moisture = SoilMoistureService.get_soil_moisture_reading(soil_moisture_percentage)

    # --------------------------- CONVERTING CROP INFORMATION ---------------------------
    crop_name = crop_information[0]
    stage_number = crop_information[1]

    crop_data = CropInfo.general_crop_info(crop_name)
    crop_id = crop_data["_id"]
    stage = crop_data["cropGrowthStage"]["stages"][stage_number - 1]["stage"]
    water_use = crop_data["cropGrowthStage"]["stages"][stage_number - 1]["waterUse"]

    crop_stage = Crop.Stage(stage_number, stage, water_use)
    crop_info = SelectedCrop.SelectedCrop(crop_name, crop_id, crop_stage)

    # --------------------------- FORMING WEATHER INFORMATION ---------------------------
    lat, lon = coordinates
    weather_data = WeatherDataService.get_today_weather_data(lat, lon, language)
    weather_info = WeatherDataService.create_today_weather(weather_data)

    # --------------------------- FINAL CALCULATION ---------------------------
    water_advice = WaterAdviceService.create_water_advice(weather_info, crop_info, soil_moisture)
    final_decision = water_advice.watering_decision
    water_advice.watering_decision = variables[final_decision]

    speech = SpeechAdvice.speech_advice(language, soil_moisture.soil_moisture_percentage, water_advice.temperature,
                                        water_advice)
    Watson.text2speech(speech)
    playsound("test.mp3", True)
    return Translation.translated_final_advice(language, water_advice)


sensora(50, "en", ("corn", 2), (43.324, 123.43))
