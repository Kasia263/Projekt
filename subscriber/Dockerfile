# Używamy oficjalnego obrazu Pythona
FROM python:3.9-slim

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Kopiowanie plików do obrazu
COPY subscriber.py .
COPY /templates/index.html .
COPY MQTTSubscriber.py .
COPY dane.txt .

# Instalacja wymaganych bibliotek
RUN pip install paho-mqtt flask

# Uruchomienie programu
CMD ["python", "subscriber.py"]