import os
import json
import paho.mqtt.client as mqtt
from datetime import datetime
from dotenv import load_dotenv

class MQTTSubscriber:
    def __init__(self):
        # Ładowanie zmiennych środowiskowych
        load_dotenv()
        self.broker_address = os.getenv('BROKER_ADDRESS')
        self.broker_port = int(os.getenv('BROKER_PORT'))
        self.mqtt_user = os.getenv('MQTT_USER')
        self.mqtt_password = os.getenv('MQTT_PASSWORD')
        self.topic_pattern = "#"
        self.client = mqtt.Client()
        
        if not all([self.broker_address, self.broker_port, self.mqtt_user, self.mqtt_password]):
            print("Error: Missing one or more environment variables.")
            exit(1)

        # Ustawienie client 
        if self.mqtt_user and self.mqtt_password:
            self.client.username_pw_set(self.mqtt_user, self.mqtt_password)
        
        # Przypisywaniem metod
        self.client.on_connect = self.on_connect #Przypisuje metodę self.on_connect jako funkcję obsługującą zdarzenie połączenia klienta MQTT z brokerem.
        self.client.on_message = self.on_message #Przypisuje metodę self.on_message jako funkcję obsługującą zdarzenie odebrania wiadomości.

        # Folder na pliki
        self.data_folder = 'dane'
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    def on_connect(self, client, userdata, flags, rc):
        """Callback dla połączenia z brokerem."""
        print(f"Połączono z brokerem, kod: {rc}")
        client.subscribe(self.topic_pattern)

    def on_message(self, client, userdata, msg):
        """Callback dla otrzymanej wiadomości."""
        print(f"Otrzymano wiadomość na temacie {msg.topic}: {msg.payload.decode()}")
        
        # Zapis do pliku JSON
        self.save_to_json(msg.topic, msg.payload.decode())

    def save_to_json(self, topic, message):
        """Zapisuje dane do pliku JSON."""
        topic_parts = topic.split("/")
        if len(topic_parts) >= 2:
            student_id = topic_parts[0]
            location = topic_parts[1]
            file_name = f"{student_id}-{location}.json"
        else:
            file_name = "unknown.json"
        
        file_path = os.path.join(self.data_folder, file_name)
        data = {
            'topic': topic,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }

        # Zapisywanie danych do pliku JSON
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def start(self):
        """Uruchamia subskrybenta."""
        print("Łączenie z brokerem...")
        self.client.connect(self.broker_address, self.broker_port)
        self.client.loop_forever()

# Inicjowanie i uruchamianie subskrybenta
if __name__ == "__main__":
    subscriber = MQTTSubscriber()
    subscriber.start()
