class DayPart:
    def __init__(self, cloud_cover=None, day_or_night=None, daypart_name=None, icon_code=None, icon_code_extend=None, narrative=None, precip_chance=None, precip_type=None,
                 qpf=None, qpf_snow=None, qualifier_code=None, relative_humidity=None, snow_range=None, temperature=None, temperature_heat_index=None,
                 temperature_wind_chill=None, thunder_category=None, thunder_index=None, uv_description=None, uv_index=None, wind_direction=None,
                 wind_direction_cardinal=None, wind_phrase=None, wind_speed=None, wx_phrase_long=None, wx_phrase_short=None):
        self.cloud_cover = cloud_cover
        self.day_or_night = day_or_night
        self.daypart_name = daypart_name
        self.icon_code = icon_code
        self.icon_code_extend = icon_code_extend
        self.narrative = narrative
        self.precip_chance = precip_chance
        self.precip_type = precip_type
        self.qpf = qpf
        self.qpf_snow = qpf_snow
        self.qualifier_code = qualifier_code
        self.relative_humidity = relative_humidity
        self.snow_range = snow_range
        self.temperature = temperature
        self.temperature_heat_index = temperature_heat_index
        self.temperature_wind_chill = temperature_wind_chill
        self.thunder_category = thunder_category
        self.thunder_index = thunder_index
        self.uv_description = uv_description
        self.uv_index = uv_index
        self.wind_direction = wind_direction
        self.wind_direction_cardinal = wind_direction_cardinal
        self.wind_phrase = wind_phrase
        self.wind_speed = wind_speed
        self.wx_phrase_long = wx_phrase_long
        self.wx_phrase_short = wx_phrase_short


class Data:
    def __init__(self, day_of_week=None, narrative=None, qpf=None, qpf_snow=None, sunrise_time_local=None, sunrise_time_utc=None, sunset_time_local=None,
                 sunset_time_utc=None, temperature_max=None, temperature_min=None, valid_time_local=None, valid_time_utc=None, day_part=None):
        self.day_of_week = day_of_week
        self.narrative = narrative
        self.qpf = qpf
        self.qpf_snow = qpf_snow
        self.sunrise_time_local = sunrise_time_local
        self.sunrise_utc = sunrise_time_utc
        self.sunset_time_local = sunset_time_local
        self.sunset_time_utc = sunset_time_utc
        self.temperature_max = temperature_max
        self.temperature_min = temperature_min
        self.valid_time_local = valid_time_local
        self.valid_time_utc = valid_time_utc
        self.day_part = day_part


class WeatherResponse:
    def __init__(self, data=None):
        self.data = data
