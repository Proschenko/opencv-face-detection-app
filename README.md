
# OpenCV Face Detection App

Это Python-приложение, упакованное в Docker-образ, которое обнаруживает лица на изображении с использованием библиотеки OpenCV. Автоматизированная сборка и публикация образа на DockerHub осуществляется средствами GitHub Actions.

## Описание

Приложение загружает изображение из репозитория, обрабатывает его и обнаруживает лица с помощью каскадного классификатора Хаара. Обнаруженные лица подсчитываются и результат выводится в стандартный вывод (stdout).

## Как использовать

### Локальный запуск

1. Убедитесь, что у вас установлен Python 3 и OpenCV.
2. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/your-username/opencv-face-detection-app.git
    cd opencv-face-detection-app
    ```
3. Установите зависимости:
    ```bash
    pip install opencv-python-headless
    ```
4. Запустите приложение:
    ```bash
    python face_detection.py
    ```

### Запуск с использованием Docker

1. Сборка Docker-образа:
    ```bash
    docker build -t opencv-face-detection-app .
    ```
2. Запуск контейнера:
    ```bash
    docker run --rm opencv-face-detection-app
    ```

### Автоматическая сборка и публикация Docker-образа

Репозиторий настроен для автоматической сборки и публикации Docker-образа в DockerHub с использованием GitHub Actions. При каждом пуше в основную ветку образ автоматически собирается и отправляется в DockerHub.

## Настройка GitHub Actions

Чтобы настроить автоматическую публикацию Docker-образа в DockerHub:

1. Добавьте секреты `DOCKER_USERNAME` и `DOCKER_PASSWORD` в настройки вашего репозитория на GitHub.
2. Убедитесь, что файл `.github/workflows/docker-image.yml` настроен на публикацию образа с вашим именем пользователя DockerHub.

## Требования

- Python 3.9 или выше
- OpenCV (устанавливается в Docker-образе)

## Пример использования

После запуска приложение выведет количество обнаруженных лиц на изображении. Этот простой пример демонстрирует, как использовать OpenCV для базового анализа изображений.

## Лицензия

Этот проект распространяется под лицензией MIT.