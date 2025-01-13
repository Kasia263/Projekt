import paho.mqtt.client as mqtt
import os
import WeatherRequester

class MQTTPublisher:

    def __init__(self, city,BROKER_ADDRESS,BROKER_PORT,MQTT_USER,MQTT_PASSWORD,STUDENT_ID,TOPIC):
        self.city = city
        self.weather_requester = WeatherRequester.WeatherRequester(city)
        self.BROKER_ADDRESS = BROKER_ADDRESS
        self.BROKER_PORT = BROKER_PORT
        self.MQTT_USER = MQTT_USER
        self.MQTT_PASSWORD = MQTT_PASSWORD
        self.STUDENT_ID = STUDENT_ID
        self.TOPIC = TOPIC

    def connect_mqtt(self):
        client = mqtt.Client()
        client.username_pw_set(self.MQTT_USER, self.MQTT_PASSWORD)
        client.connect(self.BROKER_ADDRESS, self.BROKER_PORT)
        return client

    def publish_weather(self):
        weather_data = self.weather_requester.fetch_weather()
        client = self.connect_mqtt()
        client.publish(self.TOPIC, weather_data)
        client.disconnect()
        print(f"Opublikowano dane na temat: {self.TOPIC}")