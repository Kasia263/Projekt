import paho.mqtt.client as mqtt
import os
import WeatherRequester

class MQTTPublisher:

    def __init__(self, city):
        self.city = city
        self.weather_requester = WeatherRequester(city)
        self.broker = os.getenv('BROKER', 'localhost')
        self.port = int(os.getenv('PORT', 1883))
        self.user = os.getenv('MQTT_USER', 'user')
        self.password = os.getenv('MQTT_PASSWORD', 'password')

    def connect_mqtt(self):
        client = mqtt.Client()
        client.username_pw_set(self.user, self.password)
        client.connect(self.broker, self.port)
        return client

    def publish_weather(self):
        weather_data = self.weather_requester.fetch_weather()
        client = self.connect_mqtt()
        topic = f"weather/{self.city}/current"
        client.publish(topic, weather_data)
        client.disconnect()
        print(f"Opublikowano dane na temat: {topic}")