import paho.mqtt.client as mqtt

class MQTTSubscriber:

    def __init__(self, BROKER_ADDRESS, BROKER_PORT, MQTT_USER, MQTT_PASSWORD, STUDENT_ID, TOPIC):
        self.BROKER_ADDRESS = BROKER_ADDRESS
        self.BROKER_PORT = BROKER_PORT
        self.MQTT_USER = MQTT_USER
        self.MQTT_PASSWORD = MQTT_PASSWORD
        self.STUDENT_ID = STUDENT_ID
        self.TOPIC = TOPIC

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
        print(f"Otrzymano wiadomość na temacie: {message.topic}")
        print(f"Payload: {message.payload.decode('utf-8')}")

    def start_subscription(self):
        client = self.connect_mqtt()
        client.loop_forever()