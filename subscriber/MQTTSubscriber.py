import paho.mqtt.client as mqtt

class MQTTSubscriber:

    def __init__(self, BROKER_ADDRESS, BROKER_PORT, MQTT_USER, MQTT_PASSWORD, STUDENT_ID, TOPIC, LOG_FILE):
        self.BROKER_ADDRESS = BROKER_ADDRESS
        self.BROKER_PORT = BROKER_PORT
        self.MQTT_USER = MQTT_USER
        self.MQTT_PASSWORD = MQTT_PASSWORD
        self.STUDENT_ID = STUDENT_ID
        self.TOPIC = TOPIC
        self.LOG_FILE = LOG_FILE  # Nazwa pliku logu

    def connect_mqtt(self):
        client = mqtt.Client()
        client.username_pw_set(self.MQTT_USER, self.MQTT_PASSWORD)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        try:
            client.connect(self.BROKER_ADDRESS, self.BROKER_PORT)
            print(f"Połączono z brokerem MQTT: {self.BROKER_ADDRESS}:{self.BROKER_PORT}")
        except Exception as e:
            print(f"Nie udało się połączyć z brokerem: {e}")
            raise
        return client

    def on_connect(self, client, userdata, flags, rc):
        print(f"Połączono z brokerem z kodem: {rc}")
        result, mid = client.subscribe(self.TOPIC)
        if result == mqtt.MQTT_ERR_SUCCESS:
            print(f"Subskrypcja powiodła się dla tematu: {self.TOPIC}")
        else:
            print(f"Nie udało się subskrybować tematu: {self.TOPIC}")

    def on_message(self, client, userdata, message):
        payload = message.payload.decode('utf-8')
        print(f"Otrzymano wiadomość na temacie: {message.topic}")
        print(f"Payload: {payload}")
        
        # Zapis do pliku
        with open(self.LOG_FILE, "a") as log_file:
            log_file.write(f"Temat: {message.topic}\n")
            log_file.write(f"Wiadomość: {payload}\n")
            log_file.write("-" * 40 + "\n")

    def start_subscription(self):
        client = self.connect_mqtt()
        client.loop_forever()
