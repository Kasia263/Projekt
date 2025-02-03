import MqttPublisher as mp
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="dane.env")
BROKER_ADDRESS = os.getenv('BROKER_ADDRESS')
BROKER_PORT = int(os.getenv('BROKER_PORT'))
MQTT_USER = os.getenv('MQTT_USER')
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD')
STUDENT_ID = os.getenv('STUDENT_ID')
CITY = os.getenv('CITY')
TOPIC = f"{STUDENT_ID}/{CITY}"
OPENAQ_API_KEY = os.getenv('OPENAQ_API_KEY')

if not all([BROKER_ADDRESS, BROKER_PORT, MQTT_USER, MQTT_PASSWORD,STUDENT_ID,CITY,OPENAQ_API_KEY]):
    print("Error: Missing one or more environment variables.")
    exit(1)

if __name__ == "__main__":
    mqtt = mp.MqttPublisher(CITY, BROKER_ADDRESS, BROKER_PORT, MQTT_USER, MQTT_PASSWORD, STUDENT_ID, TOPIC,OPENAQ_API_KEY)
    mqtt.start_publishing()