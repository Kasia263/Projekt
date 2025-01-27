# Używamy oficjalnego obrazu Pythona
FROM python:3.9-slim

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Kopiowanie plików do obrazu
COPY publisher.py .
COPY MqttPublisher.py .
COPY WeatherRequester.py .

# Instalacja wymaganych bibliotek
RUN pip install paho-mqtt

# Uruchomienie programu
CMD ["python", "publisher.py"]