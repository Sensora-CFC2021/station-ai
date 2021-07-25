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
    return date_time.date()  # format: yyyy-mm-dd


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
    current_time = get_current_time_in_milliseconds(datetime.datetime.now())
    rise_time = datetime.time(sunrise_time)  # assuming that sunrise time, and sunset time is in tuple format
    set_time = datetime.time(sunset_time)

    format_sunrise_time = get_current_time_in_milliseconds(rise_time)
    format_sunset_time = get_current_time_in_milliseconds(set_time)

    if format_sunrise_time <= current_time < format_sunset_time:
        return True
    else:
        return False
