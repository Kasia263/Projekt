import json 
import datetime
import requests

class WeatherRequester:

    def __init__(self, adres):
        self.adres = adres
        self.time = datetime.datetime.now().isoformat()
        self.api_key = '613ddb223dcfb9d0cb517f7e60de09080939dc8a3d13eec0e7ff3d726dcd9873'

    def pobieranie(self):
        url = ''
        r = requests.get(url)
        if r.status_code = 200:
            msg = r.json()
            print(msg)
#            mqtt.client.publish()
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={},canada&APPID={}'.format(self.adres, apikey))
        return(r.text)
        self.time = datetime.datetime.now().isoformat()
        data = {'location':self.adres, 
                'timestamp':self.time,
                'values':[]}
        data_to_send = json.dumps(data)
        print(data_to_send)