import MqttPublisher as mp

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "test/mqtt_project/data"
city = "Tokyo"

if __name__ == "__main__":  
    publisher = mp.MqttPublisher(BROKER, PORT, TOPIC, city)
    publisher.start_publishing()