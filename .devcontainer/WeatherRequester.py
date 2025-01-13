import requests

class WeatherRequester:

    def __init__(self, city):
        self.city = city
        self.API_KEY = "ae4554e4be09aaf8a7553cb4ac94b8f9"
        self.BASE_URL = "http://api.weatherstack.com/current"

    def fetch_weather(self):
        params = {
            "access_key": self.API_KEY,
            "query": self.city
        }
        response = requests.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                return f"Błąd: {data['error']['info']}"
            else:
                return self.format_weather(data)
        else:
            return "Nie udało się połączyć z API."
    
    def format_weather(self,data):
        location = data["location"]["name"]
        country = data["location"]["country"]
        temperature = data["current"]["temperature"]
        description = data["current"]["weather_descriptions"][0]
        wind_speed = data["current"]["wind_speed"]
        humidity = data["current"]["humidity"]

        return (
            f"Pogoda dla: {location}, {country}\n"
            f"Temperatura: {temperature}°C\n"
            f"Opis: {description}\n"
            f"Prędkość wiatru: {wind_speed} km/h\n"
            f"Wilgotność: {humidity}%"
        )