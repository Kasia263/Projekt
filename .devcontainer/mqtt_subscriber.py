import paho.mqtt.client as mqtt
import os

class MQTTSubscriber:

    def __init__(self,BROKER_ADDRESS,BROKER_PORT,MQTT_USER,MQTT_PASSWORD,STUDENT_ID,TOPIC):
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
    
    def on_message(self, client, userdata, message):
        # Przetwarzanie danych i zapis na dysku
        topic = message.self.TOPIC
        payload = message.payload.decode('utf-8')
        # Zakładamy, że topic ma format: weather/<miasto>/current
        topic_parts = topic.split('/')
        student_id = topic_parts[1]  # Pierwsza część tematu to numer studenta
        location = topic_parts[2]   # Druga część to lokalizacja

        # Tworzenie pliku i zapis danych
        file_name = f"{student_id}-{location}.txt"
        with open(file_name, 'w') as file:
            file.write(f"Dane z tematu: {topic}\n")
            file.write(f"Dane: {payload}\n")
        print(f"Zapisano dane do pliku: {file_name}")

    def start_subscription(self):
        client = self.connect_mqtt()
        client.on_message = self.on_message

        # Subskrypcja z użyciem Wildcards
        client.subscribe("weather/+/current")  # + to wildcard dla dowolnego studenta
        client.loop_forever()  # Czeka na wiadomości