import paho.mqtt.client as mqtt
import time
import json
import WeatherRequester as w

class MqttPublisher:
    def __init__(self, city, broker, port, user, password, student_id, topic):
        self.WeatherRequester = w.WeatherRequester(city)
        self.broker = broker
        self.port = port
        self.user = user
        self.password = password
        self.student_id = student_id
        self.topic = topic
        self.client = None
        self.actual_data = self.WeatherRequester.fetch_weather()

    def on_publish(self, client, userdata, mid):
        print(f"Message published with mid: {mid}")

    def setup_client(self):
        #"""Ustawienie MQTT/ protokół MQTTv5 ."""
        print (self.broker)
        self.client = mqtt.Client(client_id="Publisher", protocol=mqtt.MQTTv5)
        self.client.username_pw_set(self.user, self.password)
        self.client.on_publish = self.on_publish  
        self.client.connect(self.broker, self.port, 60)

    def publish_data(self):
        #"""Publikacja danych"""
        data = self.actual_data
        self.client.publish(self.topic, json.dumps(data))
        print(f"Published: {data}")
        time.sleep(5)

    def start_publishing(self):
        #"""Start the publishing loop."""
        try:
            while True:
                self.actual_data = self.WeatherRequester.fetch_weather()
                if self.client is None or not self.client.is_connected():
                    self.setup_client()
                self.publish_data()
        except KeyboardInterrupt:
            print("Stopping Publisher...")
            if self.client:
                self.client.disconnect()
