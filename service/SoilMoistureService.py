from models import SoilMoisture


def get_soil_moisture_reading(value_percentage):
    soil_moisture = SoilMoisture.SoilMoisture(0, "")
    soil_moisture_reading_percentage = value_percentage

    soil_moisture.soil_moisture_percentage = soil_moisture_reading_percentage

    if soil_moisture.soil_moisture_percentage <= 33:
        soil_moisture.soil_moisture_index = "LOW"
    elif 33 < soil_moisture.soil_moisture_percentage <= 66:
        soil_moisture.soil_moisture_index = "MEDIUM"
    else:
        soil_moisture.soil_moisture_index = "HIGH"

    return soil_moisture
