class DateTimeUtil:
    @staticmethod
    def is_today(date):
        today_date = None  # need formatting
        if date == today_date:
            return True
        else:
            return False

    def extract_date_from_date_time(self, date_time):  # to change
        pass

    @staticmethod
    def get_current_time_in_milliseconds():
        return Date().get_time()

    @staticmethod
    def is_day_time(sunrise_time, sunset_time):
        current_time = Date().get_time()
        format_sunrise_time = Date(sunrise_time).get_time()
        format_sunset_time = Date(sunset_time).get_time()

        if format_sunrise_time <= current_time < format_sunset_time:
            return True
        else:
            return False
