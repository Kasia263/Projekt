import threading
from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# Klasa do zarządzania tekstami
class TextManager:
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def set_text(self, new_text):
        self.text = new_text

# Inicjalizacja obiektu TextManager
text_manager = TextManager("Początkowy tekst")

# Przykład klasy, która będzie zmieniała tekst co pewien czas (np. z MQTT lub innej logiki)
class TextUpdater(threading.Thread):
    def __init__(self, text_manager):
        threading.Thread.__init__(self)
        self.text_manager = text_manager

    def run(self):
        while True:
            # Symulacja zmiany tekstu (np. z MQTT)
            new_text = "Nowy tekst"  # Możesz tutaj dodać kod do odbierania nowych danych
            self.text_manager.set_text(new_text)
            time.sleep(5)  # Czeka 5 sekund przed zmianą tekstu

# Uruchomienie wątku do aktualizacji tekstu
text_updater = TextUpdater(text_manager)
text_updater.start()

@app.route('/')
def home():
    # Przekazanie aktualnego tekstu do szablonu
    return render_template('index.html', text=text_manager.get_text())

@app.route('/get_text')
def get_text():
    # Zwracanie tekstu w formie JSON
    text = text_manager.get_text()
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
