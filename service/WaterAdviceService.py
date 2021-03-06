from models import SoilMoisture, Advice
from utilities import DateTimeUtil
from service import WeatherDataService


def create_water_advice(weather_info, crop_info, soil_moisture):
    soil_moisture = SoilMoisture.SoilMoisture(soil_moisture.soil_moisture_percentage, soil_moisture.soil_moisture_index)
    water_advice = Advice.WaterAdvice(crop_info.stage.water_use, crop_info.stage.stage, crop_info.crop_id,
                                      crop_info.crop_name, soil_moisture)
    is_day_time = DateTimeUtil.is_day_time(weather_info.sunrise_time, weather_info.sunset_time)

    if is_day_time:
        water_advice.temperature = weather_info.day_time.temperature
        water_advice.watering_decision = generate_water_advice(weather_info.day_time, soil_moisture.soil_moisture_index)

    else:
        water_advice.temperature = weather_info.night_time.temperature
        water_advice.watering_decision = generate_water_advice(weather_info.night_time,
                                                               soil_moisture.soil_moisture_index)

    return water_advice


def generate_water_advice(weather_info, soil_moisture_index):

    if WeatherDataService.is_raining(weather_info):
        rain_index = WeatherDataService.determine_rain_index(weather_info.precip_chance)
        return determine_rainy_day_advice(rain_index, soil_moisture_index)

    else:
        temperature_index = WeatherDataService.determine_temperature_index(weather_info.temperature)
        return determine_non_rainy_day_advice(soil_moisture_index, temperature_index)


def determine_rainy_day_advice(rain_index, soil_moisture_index):
    if rain_index == "LOW" and soil_moisture_index == "LOW":
        return "WATER_CROPS"
    elif rain_index == "LOW" and soil_moisture_index == "MEDIUM":
        return "WATER_CROPS_LESS"
    elif rain_index == "LOW" and soil_moisture_index == "HIGH":
        return "DONT_WATER"
    elif rain_index == "MEDIUM" and soil_moisture_index == "LOW":
        return "WATER_CROPS"
    elif rain_index == "MEDIUM" and soil_moisture_index == "MEDIUM":
        return "WATER_CROPS_LESS"
    elif rain_index == "MEDIUM" and soil_moisture_index == "HIGH":
        return "DONT_WATER"
    elif rain_index == "HIGH" and soil_moisture_index == "LOW":
        return "DONT_WATER"
    elif rain_index == "HIGH" and soil_moisture_index == "MEDIUM":
        return "DONT_WATER"
    elif rain_index == "HIGH" and soil_moisture_index == "HIGH":
        return "DONT_WATER"
    else:
        return "DEFAULT_WATER_CROPS"


def determine_non_rainy_day_advice(soil_moisture_index, temperature_index):
    if soil_moisture_index == "LOW" and temperature_index == "LOW":
        return "WATER_CROPS"
    elif soil_moisture_index == "LOW" and temperature_index == "OPTIMUM":
        return "WATER_CROPS"
    elif soil_moisture_index == "LOW" and temperature_index == "MEDIUM":
        return "WATER_CROPS"
    elif soil_moisture_index == "LOW" and temperature_index == "HIGH":
        return "WATER_CROPS_MORE"
    elif soil_moisture_index == "MEDIUM" and temperature_index == "LOW":
        return "DONT_WATER"
    elif soil_moisture_index == "MEDIUM" and temperature_index == "OPTIMUM":
        return "WATER_CROPS"
    elif soil_moisture_index == "MEDIUM" and temperature_index == "MEDIUM":
        return "WATER_CROPS"
    elif soil_moisture_index == "MEDIUM" and temperature_index == "HIGH":
        return "WATER_CROPS_MORE"
    elif soil_moisture_index == "MEDIUM" and temperature_index == "LOW":
        return "DONT_WATER"
    elif soil_moisture_index == "HIGH" and temperature_index == "LOW":
        return "DONT_WATER"
    elif soil_moisture_index == "HIGH" and temperature_index == "OPTIMUM":
        return "DONT_WATER"
    elif soil_moisture_index == "HIGH" and temperature_index == "MEDIUM":
        return "DONT_WATER"
    elif soil_moisture_index == "HIGH" and temperature_index == "HIGH":
        return "WATER_CROPS_LESS"
    else:
        return "DEFAULT_WATER_CROPS"


# print(determine_rainy_day_advice("LOW", "HIGH")) - testing
# print(determine_non_rainy_day_advice("LOW", "HIGH")) - testing
