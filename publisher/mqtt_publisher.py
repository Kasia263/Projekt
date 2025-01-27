import paho.mqtt.client as mqtt
import time
import json

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "test/mqtt_project/data"

def publish_data(client):
    data = {"temperature": 22.5, "humidity": 60, "status": "OK"}
    client.publish(TOPIC, json.dumps(data))
    print(f"Published: {data}")
    time.sleep(5)

def setup_publisher():
    client = mqtt.Client("Publisher")
    client.connect(BROKER, PORT)
    print(f"Connected to MQTT Broker: {BROKER}")
    return client

if __name__ == "__main__":
    client = setup_publisher()
    try:
        while True:
            publish_data(client)
    except KeyboardInterrupt:
        print("Stopping Publisher...")