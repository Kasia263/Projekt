import requests
from datetime import datetime
import pytz

class WeatherRequester:
    def __init__(self, lokalizacja,api_key):
        self.lokalizacja = lokalizacja
        self.measurements = 0
        self.api_url = "https://api.openaq.org/v3/locations/4003"
        self.api_key = api_key
        self.headers = {
            "X-API-Key": f"{self.api_key}"
        }

    def send_data(self):

        # Wysyłanie żądania GET do API z nagłówkami
        response = requests.get(self.api_url, headers=self.headers)

        # Sprawdzanie kodu odpowiedzi
        if response.status_code == 200:
            data = response.json()
            last_updated = data["results"][0]["datetimeLast"]["local"]
            sensors = data["results"][0]["sensors"][0]
            sensors_id = sensors["id"]
            

            measurements_url = f"https://api.openaq.org/v3/sensors/{sensors_id}/measurements?limit=1"
            response_2 = requests.get(measurements_url, headers=self.headers)

            #Sprawdzanie kodu odpowiedzi
            if response.status_code == 200:
                measurements_data = response_2.json()        
                self.measurements = measurements_data["results"][0]


                # Pobieranie aktualnego czasu systemowego w strefie czasowej Polski
            system_timestamp = datetime.now(pytz.utc).astimezone(pytz.timezone("Europe/Warsaw")).isoformat()
            # Tworzymy sformatowaną wiadomość
            msg = {
                "location": self.lokalizacja,
                "timestamp": system_timestamp, # Używamy aktualnego czasu systemowego w polskiej strefie czasowej
                "lastUpdated_from_api": last_updated, 
                "values": [self.measurements["parameter"]["name"], self.measurements["value"], self.measurements["parameter"]["units"]]                   
            }
            return msg
                    