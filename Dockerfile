FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev && \
    pip install opencv-python-headless

WORKDIR /app
COPY face_detection.py /app/
COPY sample1.jpg /app/


CMD ["python", "face_detection.py"]
