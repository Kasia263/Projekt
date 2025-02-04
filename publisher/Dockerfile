# Wybieramy obraz bazowy
FROM python:3.9-slim

# Ustalamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy pliki z folderu 'publisher' do katalogu roboczego w kontenerze
COPY publisher/ /app/publisher/

# Instalujemy zależności z pliku requirements.txt
COPY publisher/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Kopiujemy plik .env z katalogu głównego projektu
COPY .env /app/  
# Upewniamy się, że plik .env jest w głównym katalogu projektu

# Ustawiamy komendę, która uruchomi aplikację
CMD ["python", "publisher/publisher.py"]
