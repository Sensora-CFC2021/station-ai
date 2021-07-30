def speech_advice(language, soil_moisture_percentage, temperature, water_advice):
    result = "Soil moisture is " + str(soil_moisture_percentage) + "percent<break time='1s'/>" + \
             "Temperature is " + str(temperature) + "celsius<break time='1s'/>" + \
             "Watering advice " + str(water_advice.watering_decision) + " "
    return result
