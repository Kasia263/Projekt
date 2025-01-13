import mqtt_publisher as mp
import os
import mqtt_subscriber as ms


city = os.getenv("LOCATIONS", "Tokyo")
BROKER_ADDRESS = os.getenv("BROKER_ADDRESS", "167.172.164.168")
BROKER_PORT = int(os.getenv("BROKER_PORT", 1883))
MQTT_USER = os.getenv("MQTT_USER", "student")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", "sys-wbud")
STUDENT_ID = os.getenv("STUDENT_ID", "261334")
TOPIC = f"{STUDENT_ID}/{city}"


mqtt = mp.MQTTPublisher(city,BROKER_ADDRESS,BROKER_PORT,MQTT_USER,MQTT_PASSWORD,STUDENT_ID,TOPIC)
#mqtt.publish_weather()
subscriber = ms.MQTTSubscriber(BROKER_ADDRESS, BROKER_PORT, MQTT_USER, MQTT_PASSWORD, STUDENT_ID, TOPIC)
subscriber.start_subscription()
