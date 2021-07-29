import datetime


def is_today(date):
    today_date = datetime.today().strftime("%Y-%m-%d")
    if date == today_date:
        return True
    else:
        return False


def extract_date_from_date_time(date_time):
    """
    extract date from datetime object
    """
    year = int(date_time[:4])
    month = int(date_time[5:7])
    day = int(date_time[8:10])

    new_date_time = datetime.datetime(year, month, day)
    return new_date_time.date()  # format: yyyy-mm-dd


def get_current_time_in_milliseconds(time):
    """
    time: datetime object containing hour, minute, and second
    """
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    result = hour * 3600 + minute * 60 + second
    return result


def is_day_time(sunrise_time, sunset_time):
    sunrise_hour = int(sunrise_time[11:13])
    sunrise_minute = int(sunrise_time[14:16])
    sunrise_second = int(sunrise_time[17:19])

    sunset_hour = int(sunset_time[11:13])
    sunset_minute = int(sunset_time[14:16])
    sunset_second = int(sunset_time[17:19])

    current_time = get_current_time_in_milliseconds(datetime.datetime.now())
    rise_time = datetime.time(sunrise_hour, sunrise_minute, sunrise_second)  # assuming that sunrise time, and sunset time is in tuple format
    set_time = datetime.time(sunset_hour, sunset_minute, sunset_second)

    format_sunrise_time = get_current_time_in_milliseconds(rise_time)
    format_sunset_time = get_current_time_in_milliseconds(set_time)

    if format_sunrise_time <= current_time < format_sunset_time:
        return True
    else:
        return False
