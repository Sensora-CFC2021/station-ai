import requests
import os
from utilities import DateTimeUtil
from models import TodayWeather


WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
URL = 'https://api.weather.com/v3/wx/forecast/daily/5day?geocode={latitude}%2C{' \
      'longitude}&format=json&units=m&language={lan}&apiKey='
weather_weekly_api = URL + WEATHER_API_KEY


def get_today_weather(lat, lon, language):
    weather_data = get_today_weather_data(lat, lon, language)
    today = create_today_weather(weather_data)
    return today


def get_today_weather_data(lat=43.324, lon=123.43, language="mn"):
    response = requests.get(weather_weekly_api.format(latitude=lat, longitude=lon, lan=language))
    weather_data = response.json()
    return weather_data


def create_today_weather(weather_info):
    today = TodayWeather.TodayWeather()

    today.day_of_week = weather_info["dayOfWeek"][0]
    today.narrative = weather_info["narrative"][0]
    today.sunrise_time = weather_info["sunriseTimeLocal"][0]
    today.sunset_time = weather_info["sunsetTimeLocal"][0]
    today.max_temperature = weather_info["temperatureMax"][0]
    today.min_temperature = weather_info["temperatureMin"][0]
    today.date = DateTimeUtil.extract_date_from_date_time(weather_info["validTimeLocal"][0])

    day_part = weather_info["daypart"][0]

    day_time = TodayWeather.WeatherInfo()
    day_time.narrative = day_part["narrative"][1]
    day_time.precip_chance = day_part["precipChance"][1]
    day_time.precip_type = day_part["precipType"][1]
    day_time.humidity = day_part["relativeHumidity"][1]
    day_time.temperature = day_part["temperature"][1]
    day_time.wind_speed = day_part["windSpeed"][1]

    today.day_time = day_time

    night_time = TodayWeather.WeatherInfo()
    night_time.narrative = day_part["narrative"][2]
    night_time.precip_chance = day_part["precipChance"][2]
    night_time.precip_type = day_part["precipType"][2]
    night_time.humidity = day_part["relativeHumidity"][2]
    night_time.temperature = day_part["temperature"][2]
    night_time.wind_speed = day_part["windSpeed"][2]

    today.night_time = night_time

    return today


def is_raining(weather_info):
    if weather_info.precip_type == "rain" or weather_info.precip_type == "precip":
        if weather_info.precip_chance > 25:
            return True
        else:
            return False
    else:
        return False


def determine_temperature_index(temp):
    print("temp", temp)
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
