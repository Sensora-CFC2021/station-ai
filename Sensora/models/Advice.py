class WaterAdvice:
    def __init__(self, water_recommended=None, stage=None, crop_id=None, crop_name=None, soil_moisture_reading=None):
        self.water_recommended = water_recommended
        self.stage = stage
        self.id = crop_id
        self.crop_name = crop_name
        self.soil_moisture_reading = soil_moisture_reading
