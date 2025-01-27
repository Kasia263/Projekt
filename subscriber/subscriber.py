import paho.mqtt.client as mqtt
import json
import os

# Pobieranie danych z zmiennych środowiskowych
BROKER_ADDRESS = os.getenv("BROKER_ADDRESS", "167.172.164.168")
BROKER_PORT = int(os.getenv("BROKER_PORT", 1883))
MQTT_USER = os.getenv("MQTT_USER", "student")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", "sys-wbud")
TOPIC_PATTERN = "#"

# Funkcja zapisująca dane do pliku
def save_data_to_file(student_id, location, data):
    file_name = f"{student_id}-{location}.json"
    file_path = os.path.join(file_name)
    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"Data saved to {file_path}")

# Funkcja wywoływana po odebraniu wiadomości
def on_message(client, userdata, message):
    try:
        # Odbieranie topiku i danych
        topic = message.topic
        payload = message.payload.decode("utf-8")
        data = json.loads(payload)
        
        # Parsowanie topiku
        topic_parts = topic.split("/")
        student_id = topic_parts[0] # Zakładamy, że ID studenta to pierwsza część topiku
        location = topic_parts[1] # Zakładamy, że lokalizacja to druga część topiku
        
        # Zapisanie danych w pliku
        save_data_to_file(student_id, location, data)
    
    except Exception as e:
        print(f"Error processing message: {e}")

# Ustawienie klienta MQTT
client = mqtt.Client()

# Konfiguracja autentykacji
client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

# Rejestracja funkcji callback na odebrane wiadomości
client.on_message = on_message

# Połączenie z brokerem MQTT
client.connect(BROKER_ADDRESS, BROKER_PORT)

# Subskrypcja wszystkich topików (użycie wildcard #)
client.subscribe(TOPIC_PATTERN)

# Uruchomienie pętli nasłuchującej wiadomości
client.loop_forever()
