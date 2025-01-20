def analyze_weather(weather_data):
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    condition = weather_data["weather"][0]["main"]
    
    advice = []
    
    if temp > 35:
        advice.append("Stay hydrated and avoid prolonged sun exposure.")
    elif temp < 10:
        advice.append("Wear warm clothes and avoid cold exposure.")
    
    if condition.lower() in ["rain", "snow"]:
        advice.append("Carry an umbrella and wear waterproof footwear.")
    
    if humidity > 80:
        advice.append("Stay in cool places to avoid heat-related illnesses.")
    
    return advice
