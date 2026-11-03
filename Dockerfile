FROM python:3.11-slim

# Указываем рабочую папку внутри контейнера
WORKDIR /app

# Копируем скрипт в рабочую папку
COPY script.py .

CMD ["python", "script.py"]
