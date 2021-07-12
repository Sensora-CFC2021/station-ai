from huuchin import constants as constants, SoilMoisture


def get_soil_moisture_reading(soil_moisture_percentage):
    soil_moisture_info = SoilMoisture.SoilMoisture(soil_moisture_percentage, "")
    if soil_moisture_percentage <= 33:
        soil_moisture_info.set_index(constants.low)

    elif 33 < soil_moisture_percentage <= 66:
        soil_moisture_info.set_index(constants.medium)

    else:
        soil_moisture_info.set_index(constants.high)
    return soil_moisture_info
