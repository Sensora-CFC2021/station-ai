class WaterAdvice:
    def __init__(self, water_recommended, stage, crop_id, crop_name, soil_moisture_reading):
        self.water_recommended = water_recommended
        self.stage = stage
        self.id = crop_id
        self.crop_name = crop_name
        self.soil_moisture_reading = soil_moisture_reading
