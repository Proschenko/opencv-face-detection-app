import cv2


def detect_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Читаем изображение
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image.")
        return

    # Конвертируем изображение в оттенки серого для улучшения распознавания
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Находим лица на изображении
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Выводим результат
    print(f"Found {len(faces)} face(s).")
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print(f"Face №{i+1} coord:  ({x},{y}),({x+w},{y+h})")
    # Для отладки
    #cv2.imwrite(f"{image_path}_output.jpg", image)


if __name__ == "__main__":
    detect_faces("sample1.jpg")  # Замените на название вашего изображения
