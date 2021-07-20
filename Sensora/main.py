from translation import Translation
from service import SoilMoistureService, WeatherDataService, WaterAdviceService
from crop import CropInfo
from models import SelectedCrop, Crop, WeatherResponse


def sensora(soil_moisture_percentage, language, crop_information):
    """
    soil_moisture_percentage: number - integer/float,
    language: string - "en" / "mn"
    crop_information: tuple containing the crop type and its growth stage
    irrigation_night: boolean indicating when to water the crops - True, if watering the crops through the day, False, otherwise
    """

    # --------------------------- TRANSLATION VARIABLES ---------------------------
    variables = Translation.translated_advice(language)


    # --------------------------- SOIL MOISTURE, SOIL MOISTURE INDEX ---------------------------
    soil_moisture = SoilMoistureService.get_soil_moisture_reading(soil_moisture_percentage)
    soil_moisture_index = soil_moisture.soil_moisture_index


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
    weather_data = None # instance of Weather Response
    weather_info = WeatherDataService.create_today_weather(weather_data)

    precip = weather_info.precip_chance
    rain_index = WeatherDataService.determine_rain_index(precip)

    temperature = weather_info.temperature
    temperature_index = WeatherDataService.determine_temperature_index(temperature)


    # --------------------------- FINAL CALCULATION ---------------------------
    advice = WaterAdviceService.create_water_advice(weather_info, crop_info, soil_moisture)
    final_decision = advice.watering_decision
    advice.watering_decision = variables[final_decision]

    return advice


# print(sensora(90, "en", ("corn", 4)))
