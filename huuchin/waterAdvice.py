from huuchin import constants, variables
from huuchin.SoilMoisture import SoilMoisture
from huuchin.Advice import WaterAdvice
from huuchin.DateTimeUtils import DateTimeUtil


def get_water_advice():
    pass


def create_water_advice(weather_info, crop_info, soil_moisture):
    soil_moisture = SoilMoisture(soil_moisture.soil_moisture_percentage, soil_moisture.soil_moisture_index)
    water_advice = WaterAdvice(crop_info.stage.water_use, crop_info.stage.stage, crop_info.id, crop_info.crop_name,
                               soil_moisture)

    date_time_util = DateTimeUtil()  # to change
    is_day_time = date_time_util.is_day_time(weather_info.sunrise_time, weather_info.sunset_time)

    if is_day_time:
        water_advice.temperature = weather_info.day_time.temperature
        water_advice.watering_decision = generate_water_advice(weather_info.day_time, soil_moisture.soil_moisture_index)

    else:
        water_advice.temperature = weather_info.night_time.temperature
        water_advice.watering_decision = generate_water_advice(weather_info.night_time,
                                                               soil_moisture.soil_moisture_index)


def generate_water_advice(weather_info, soil_moisture_index):
    if is_raining(weather_info):
        rain_index = determine_rain_index(weather_info.precip_chance)
        return determine_rainy_day_advice(rain_index, soil_moisture_index)

    else:
        temperature_index = determine_temperature_index(weather_info.temperature)
        return determine_non_rainy_day_advice(soil_moisture_index, temperature_index)


def determine_rainy_day_advice(rain_index, soil_moisture_index):
    if rain_index == constants.low and soil_moisture_index == constants.low:
        return variables.WATER_CROPS
    elif rain_index == constants.low and soil_moisture_index == constants.medium:
        return variables.WATER_CROPS_LESS
    elif rain_index == constants.low and soil_moisture_index == constants.high:
        return variables.DONT_WATER
    elif rain_index == constants.medium and soil_moisture_index == constants.low:
        return variables.WATER_CROPS
    elif rain_index == constants.medium and soil_moisture_index == constants.medium:
        return variables.WATER_CROPS_LESS
    elif rain_index == constants.medium and soil_moisture_index == constants.high:
        return variables.DONT_WATER
    elif rain_index == constants.high and soil_moisture_index == constants.low:
        return variables.DONT_WATER
    elif rain_index == constants.high and soil_moisture_index == constants.medium:
        return variables.DONT_WATER
    elif rain_index == constants.high and soil_moisture_index == constants.high:
        return variables.DONT_WATER
    else:
        return variables.DEFAULT_WATER_CROPS


def determine_non_rainy_day_advice(soil_moisture_index, temperature_index):
    if soil_moisture_index == constants.low and temperature_index == constants.low:
        return variables.WATER_CROPS
    elif soil_moisture_index == constants.low and temperature_index == constants.optimum:
        return variables.WATER_CROPS
    elif soil_moisture_index == constants.low and temperature_index == constants.medium:
        return variables.WATER_CROPS
    elif soil_moisture_index == constants.low and temperature_index == constants.high:
        return variables.WATER_CROPS_MORE
    elif soil_moisture_index == constants.medium and temperature_index == constants.low:
        return variables.DONT_WATER
    elif soil_moisture_index == constants.medium and temperature_index == constants.optimum:
        return variables.WATER_CROPS
    elif soil_moisture_index == constants.medium and temperature_index == constants.medium:
        return variables.WATER_CROPS
    elif soil_moisture_index == constants.medium and temperature_index == constants.high:
        return variables.WATER_CROPS_MORE
    elif soil_moisture_index == constants.medium and temperature_index == constants.low:
        return variables.DONT_WATER
    elif soil_moisture_index == constants.high and temperature_index == constants.low:
        return variables.DONT_WATER
    elif soil_moisture_index == constants.high and temperature_index == constants.optimum:
        return variables.DONT_WATER
    elif soil_moisture_index == constants.high and temperature_index == constants.medium:
        return variables.DONT_WATER
    elif soil_moisture_index == constants.high and temperature_index == constants.high:
        return variables.WATER_CROPS_LESS
    else:
        return variables.DEFAULT_WATER_CROPS
