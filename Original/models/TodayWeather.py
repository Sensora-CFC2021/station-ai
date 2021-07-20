class WeatherInfo:
    def __init__(self, narrative=None, precip_chance=None, precip_type=None, humidity=None, temperature=None,
                 wind_speed=None):
        self.narrative = narrative
        self.precip_chance = precip_chance
        self.precip_type = precip_type
        self.humidity = humidity
        self.temperature = temperature
        self.wind_speed = wind_speed


class TodayWeather:
    def __init__(self, day_of_week=None, narrative=None, sunrise_time=None, sunset_time=None, max_temperature=None,
                 min_temperature=None, day_time=None, night_time=None, date=None):
        self.day_of_week = day_of_week
        self.narrative = narrative
        self.sunrise_time = sunrise_time
        self.sunset_time = sunset_time
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.day_time = day_time
        self.night_time = night_time
        self.date = date
