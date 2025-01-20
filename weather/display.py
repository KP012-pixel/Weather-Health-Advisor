from prettytable import PrettyTable

def display_health_advice(weather_data, advice):
    table = PrettyTable()
    table.field_names = ["City", "Temperature (°C)", "Humidity (%)", "Condition", "Health Tips"]
    
    city = weather_data["name"]
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    condition = weather_data["weather"][0]["main"]
    tips = " | ".join(advice)
    
    table.add_row([city, temp, humidity, condition, tips])
    print(table)