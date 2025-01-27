# Bazowy obraz Pythona
FROM python:3.9-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Instalacja niezbędnych narzędzi i bibliotek systemowych
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Skopiowanie plików projektu
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY subscriber.py .

# Uruchomienie aplikacji
CMD ["python", "subscriber.py"]
