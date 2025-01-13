import paho.mqtt.client as mqtt
import os

class MQTTSubscriber:

    def __init__(self, BROKER_ADDRESS, BROKER_PORT, MQTT_USER, MQTT_PASSWORD, STUDENT_ID, TOPIC):
        self.BROKER_ADDRESS = BROKER_ADDRESS
        self.BROKER_PORT = BROKER_PORT
        self.MQTT_USER = MQTT_USER
        self.MQTT_PASSWORD = MQTT_PASSWORD
        self.STUDENT_ID = STUDENT_ID
        self.TOPIC = TOPIC

    def connect_mqtt(self):
        # Tworzymy instancję klienta MQTT
        client = mqtt.Client()
        client.username_pw_set(self.MQTT_USER, self.MQTT_PASSWORD)

        # Definiujemy callback dla połączenia
        client.on_connect = self.on_connect
        client.on_message = self.on_message  # Przypisanie callbacku na wiadomości

        # Próbujemy połączyć się z brokerem
        try:
            client.connect(self.BROKER_ADDRESS, self.BROKER_PORT)
            print(f"Połączono z brokerem MQTT: {self.BROKER_ADDRESS}:{self.BROKER_PORT}")
        except Exception as e:
            print(f"Nie udało się połączyć z brokerem: {e}")
            raise
        return client

    def on_connect(self, client, userdata, flags, rc):
        print(f"Połączono z brokerem z kodem: {rc}")
        client.subscribe(self.TOPIC)  # Subskrybujemy temat
        print(f"Subskrybowano temat: {self.TOPIC}")  # Dodajemy logowanie

    def on_message(self, client, userdata, message):
        """
        Callback wywoływany, gdy przychodzi wiadomość na subskrybowanym temacie.
        """
        topic = message.topic
        payload = message.payload.decode('utf-8')  # Dekodujemy payload na tekst

        # Wyświetlanie danych w terminalu
        print(f"Otrzymano wiadomość na temacie: {topic}")
        print(f"Dane: {payload}")

        # Zakładamy, że topic ma format: <student_id>/<location>
        topic_parts = topic.split('/')

        if len(topic_parts) == 2:  # Sprawdzamy, czy temat składa się z dokładnie 2 części
            student_id = topic_parts[0]  # Pierwsza część tematu to numer studenta
            location = topic_parts[1]    # Druga część to lokalizacja

            # Tworzenie pliku i zapis danych
            file_name = f"{student_id}-{location}.txt"
            with open(file_name, 'w') as file:
                file.write(f"Dane z tematu: {topic}\n")
                file.write(f"Dane: {payload}\n")  # Zapisujemy także payload do pliku
            print(f"Zapisano dane do pliku: {file_name}")
        else:
            print(f"Nieprawidłowy temat: {topic}")

    def start_subscription(self):
        client = self.connect_mqtt()
        client.on_message = self.on_message
        
        # Rozpoczynamy pętlę klienta w tle, aby nasłuchiwać wiadomości.
        client.loop()
        client.disconnect()  # Zakończenie połączenia z brokerem

