from datetime import datetime


class DateTimeUtil:
    def is_today(date):
        current_date = datetime.date(datetime.now())  # 2021-07-11
        if date == current_date:
            return True
        else:
            return False


    def extract_date_from_date_time(date_time):
        pass


    def get_current_time_in_milliseconds():
        pass


    def is_day_time(sunrise_time, sunset_time):
        current_time = None  # to change
        format_sunrise_time = sunrise_time  # to change
        format_sunset_time = sunset_time  # to change

        if format_sunrise_time <= current_time < format_sunset_time:
            return True
        else:
            return False
