class Crop:
    def __init__(self, crop_id=None, crop_type=None, crop_growth_stage=None, url=None):
        self.crop_id = crop_id
        self.type = crop_type
        self.crop_growth_stage = crop_growth_stage
        self.url = url


class CropGrowthStage:
    def __init__(self, number_of_stages=None, water_measurement_metric=None, water_usage=None, stage=None):
        self.number_of_stages = number_of_stages
        self.water_measurement_metric = water_measurement_metric
        self.water_usage = water_usage
        self.stage = stage


class Stage:
    def __init__(self, stage_number=None, stage=None, water_use=None, url=None):
        self.stage_number = stage_number
        self.stage = stage
        self.water_use = water_use
        self.url = url
