FROM python:3.11-slim

WORKDIR /app

# 1. Копируем файл со списком библиотек внутрь контейнера
COPY requirements.txt .

# 2. Запускаем команду установки библиотек
RUN pip install --no-cache-dir -r requirements.txt

# 3. Копируем сам скрипт автоматизации
COPY script.py .

CMD ["python", "script.py"]