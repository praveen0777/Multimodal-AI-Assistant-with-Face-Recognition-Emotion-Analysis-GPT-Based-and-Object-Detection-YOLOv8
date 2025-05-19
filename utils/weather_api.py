import requests

def get_weather(city):
    API_KEY = "your_actual_openweathermap_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        res = requests.get(url)
        data = res.json()
        
        if data.get("main"):
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"The temperature in {city} is {temp}°C with {desc}."
        else:
            return "❌ Couldn't fetch weather data. Please check city name or API key."
    except Exception as e:
        return f"❌ Error fetching weather: {e}"
