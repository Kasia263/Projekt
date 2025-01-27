import MQTTSubscriber as mq

if __name__ == "__main__":
    subscriber = mq.MQTTSubscriber(
        BROKER_ADDRESS="test.mosquitto.org",
        BROKER_PORT=1883,
        MQTT_USER="",
        MQTT_PASSWORD="",
        STUDENT_ID="12345",
        TOPIC="test/mqtt_project/data"
    )
    subscriber.start_subscription()
