class SoilMoisture:
    def __init__(self, percentage, index):
        self.soilMoisturePercentage = percentage  # number
        self.soilMoistureIndex = index  # string

    def set_index(self, index):
        self.soilMoistureIndex = index

    def set_soil_moisture_index(self, percentage):
        self.soilMoisturePercentage = percentage
