from flask import Flask, render_template, jsonify
import threading
import time
import MQTTSubscriber as mq
import os

app = Flask(__name__)

# Klasa do zarządzania tekstami
class TextManager:
    def __init__(self, text="Początkowy tekst"):
        self.text = text

    def get_text(self):
        return self.text

    def set_text(self, new_text):
        self.text = new_text

# Funkcja do aktualizacji tekstu co 5 sekund, odczytując z pliku
def text_updater(log_file):
    while True:
        time.sleep(5)  # Czeka 5 sekund przed kolejnym odczytem
        try:
            # Odczyt ostatniej linii z pliku
            with open(log_file, "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1]  # Ostatnia wiadomość w logu
                    text_manager.set_text(last_line.strip())  # Zmienia tekst na podstawie ostatniej wiadomości
        except FileNotFoundError:
            print(f"Plik logu '{log_file}' nie został znaleziony, tworzymy nowy.")
            with open(log_file, "w") as file:
                file.write("Brak danych w logu.\n")  # Tworzymy plik z początkową treścią
        except Exception as e:
            print(f"Problem z odczytem pliku: {e}")

# Inicjalizacja obiektu TextManager
text_manager = TextManager()

# Inicjalizacja subskrybenta MQTT
subscriber = mq.MQTTSubscriber(
    BROKER_ADDRESS=os.getenv("BROKER_ADDRESS", "167.172.164.168"),
    BROKER_PORT=int(os.getenv("BROKER_PORT", 1883)),
    MQTT_USER=os.getenv("MQTT_USER", "student"),
    MQTT_PASSWORD=os.getenv("MQTT_PASSWORD", "sys-wbud"),
    STUDENT_ID=os.getenv("STUDENT_ID", "261334"),
    TOPIC=f"{os.getenv('STUDENT_ID', '261334')}/Tokyo",
    LOG_FILE="mqtt_log.txt"  
)

# Uruchomienie wątku subskrybującego MQTT w tle
mqtt_thread = threading.Thread(target=subscriber.start_subscription, daemon=True)
mqtt_thread.start()

# Uruchomienie wątku do aktualizacji tekstu w tle
text_thread = threading.Thread(target=text_updater, args=("mqtt_log.txt",), daemon=True)
text_thread.start()

@app.route('/')
def home():
    return render_template('index.html', text=text_manager.get_text())

@app.route('/get_text')
def get_text():
    return jsonify({'text': text_manager.get_text()})

if __name__ == '__main__':
    app.run(debug=True)
