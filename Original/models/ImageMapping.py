class ImageMapping:
    def __init__(self, crop=None, crop_stage_image_mapping=None):
        self.crops_map = crop
        self.crop_stage_map = crop_stage_image_mapping


class Crop:
    def __init__(self, url=None):
        self.url = url


class CropGrowthStageImageMapping:
    def __init__(self, stage_url=None):
        self.stage_url = stage_url
