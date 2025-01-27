import MqttPublisher as mp
import os
import WeatherRequester as w

BROKER_ADDRESS = os.getenv("BROKER_ADDRESS", "167.172.164.168")
BROKER_PORT = int(os.getenv("BROKER_PORT", 1883))
MQTT_USER = os.getenv("MQTT_USER", "student")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", "sys-wbud")
STUDENT_ID = os.getenv("STUDENT_ID", "261334")
city = "Tokyo"
TOPIC = f"{STUDENT_ID}/{city}"

if __name__ == "__main__":
    mqtt = mp.MqttPublisher(city, BROKER_ADDRESS, BROKER_PORT, MQTT_USER, MQTT_PASSWORD, STUDENT_ID, TOPIC)
    mqtt.start_publishing()