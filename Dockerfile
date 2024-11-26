# Используем базовый образ Python
FROM python:3.11-slim

# Устанавливаем зависимости
RUN apt-get update && \
    apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev && \
    pip install opencv-python-headless

# Копируем приложение в контейнер
WORKDIR /app
COPY face_detection.py /app/
COPY sample1.jpg /app/

# Устанавливаем команду по умолчанию для запуска скрипта
CMD ["python", "face_detection.py"]
