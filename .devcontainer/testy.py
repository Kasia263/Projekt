import WeatherRequester as wr

print("Konsolowa aplikacja pogodowa")
city = input("Podaj nazwę miasta: ")
weather = wr.WeatherRequester('Warsaw')
weather_info = weather.fetch_weather()
print("\n" + weather_info)