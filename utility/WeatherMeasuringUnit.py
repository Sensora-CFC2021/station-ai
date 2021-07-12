class WeatherMeasuringUnit:
    unit = "m"

    def __init__(self, unit):
        self.unit = unit

    def set_unit(self, unit):
        self.unit = unit
        return self.unit

    def get_unit(self):
        return self.unit
