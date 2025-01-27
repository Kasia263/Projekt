import requests
from datetime import datetime
import pytz

class WeatherRequester:
    def __init__(self, lokalizacja):
        self.lokalizacja = lokalizacja
        self.api_url = "https://api.openaq.org/v2/locations/10890"
        self.headers = {
            "X-API-Key": "613ddb223dcfb9d0cb517f7e60de09080939dc8a3d13eec0e7ff3d726dcd9873"
        }

    def send_data(self):

        # Wysyłanie żądania GET do API z nagłówkami
        response = requests.get(self.api_url, headers=self.headers)

        # Sprawdzanie kodu odpowiedzi
        if response.status_code == 200:
            data = response.json()

        # Pobieranie ostatniej aktualizacji lokalizacji (lastUpdated z results)
            last_updated = data["results"][0]["lastUpdated"]

            # Pobieranie aktualnego czasu systemowego w strefie czasowej Polski
            system_timestamp = datetime.now(pytz.utc).astimezone(pytz.timezone("Europe/Warsaw")).isoformat()

            # Tworzymy sformatowaną wiadomość
            msg = {
                "location": self.lokalizacja,
                "timestamp": system_timestamp, # Używamy aktualnego czasu systemowego w polskiej strefie czasowej
                "lastUpdated_from_api": last_updated, # Zachowujemy lastUpdated z API
                "values": [
                    # Tworzymy listę wartości pomiarów, gdzie dla każdego parametru w 'parameters' dodajemy parametry
                    {
                        param["parameter"]: param["lastValue"]
                    }
                    for param in data["results"][0]["parameters"]
                ]
            }
            return msg

                    