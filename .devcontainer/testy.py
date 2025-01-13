import WeatherRequester as wr
import mqtt_publisher as ms

print("Konsolowa aplikacja pogodowa")
city = input("Podaj nazwę miasta: ")
weather = wr.WeatherRequester('Warsaw')
mqtt = ms.MQTTPublisher()
weather_info = weather.fetch_weather()
print("\n" + weather_info)
