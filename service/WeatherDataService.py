from utility import DateTimeUtil
from models import TodayWeather

today = TodayWeather.TodayWeather()
DateTimeUtil = DateTimeUtil.DateTimeUtil()


def get_today_weather():  # to change
    pass


def create_today_weather(weather_data):
    weather_info = weather_data.data

    today.day_of_week = weather_info.day_of_week[0]
    today.narrative = weather_info.narrative[0]
    today.sunrise_time = weather_info.sunrise_time_local[0]
    today.sunset_time = weather_info.sunset_time_local[0]
    today.max_temperature = weather_info.temperature_max[0]
    today.min_temperature = weather_info.temperature_min[0]
    today.date = DateTimeUtil.extract_date_from_date_time(weather_info.valid_time_local[0])

    day_part = weather_info.daypart[0]

    day_time = TodayWeather.WeatherInfo()
    day_time.narrative = day_part.narrative[0]
    day_time.precip_chance = day_part.precip_chance[0]
    day_time.precip_type = day_part.precip_type[0]
    day_time.humidity = day_part.relative_humidity[0]
    day_time.temperature = day_part.temperature[0]
    day_time.wind_speed = day_part.wind_speed[0]

    today.day_time = day_time

    night_time = TodayWeather.WeatherInfo()
    night_time.narrative = day_part.narrative[1]
    night_time.precip_chance = day_part.precip_chance[1]
    night_time.precip_type = day_part.precip_type[1]
    night_time.humidity = day_part.relative_humidity[1]
    night_time.temperature = day_part.temperature[1]
    night_time.wind_speed = day_part.wind_speed[1]

    today.night_time = night_time

    return today


def store_today_weather_in_local_storage(today_weather):  # to change - saving to local storage
    if today_weather and DateTimeUtil.is_today(today_weather.date):
        pass


def get_today_weather_from_local_storage():  # to change - getting the weather from local storage
    pass  # to change


def is_raining(weather_info):
    if weather_info.precip_type == "rain" or weather_info.perecip_type == "precip":
        if weather_info.precip_chance > 25:
            return True
        else:
            return False
    else:
        return False


def determine_temperature_index(temp):
    if temp < 5:
        return "LOW"
    elif 5 <= temp <= 25:
        return "OPTIMUM"
    elif 25 < temp < 30:
        return "MEDIUM"
    else:
        return "HIGH"


def determine_rain_index(precip):
    if 25 <= precip < 50:
        return "LOW"
    elif 50 <= precip < 75:
        return "MEDIUM"
    else:
        return "HIGH"
