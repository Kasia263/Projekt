# Używamy obrazu Pythona jako bazowego
FROM python:3.9-slim

# Ustalamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy pliki z katalogu głównego (MQTTSubscriber.py, Flask.py, .env, requirements.txt)
COPY . /app/

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

# Kopiujemy plik .env do kontenera (jeśli jest wymagany)
COPY .env /app/

# Tworzymy folder o nazwie 'dane' i ustawiamy uprawnienia
RUN mkdir -p /app/dane && chmod 755 /app/dane

# Ustawiamy komendę, która uruchomi oba pliki: MQTTSubscriber.py i Flask.py
# Opcja z uruchomieniem MQTTSubscriber w tle, aby kontener nie zakończył działania
CMD python MQTTSubscriber.py & tail -f /dev/null
