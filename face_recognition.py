import cv2
import mediapipe as mp
from database import insert_image

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def capture_image(filename='captured_face.jpg'):
    """Capture an image from the webcam."""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not open video device")
        return None

    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
    else:
        print("Failed to capture image")
    
    cap.release()
    return filename

def detect_face(image_path):
    """Detect faces in an image."""
    image = cv2.imread(image_path)
    with mp_face_detection.FaceDetection(min_detection_confidence=0.2) as face_detection:
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = image.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face_img_name = 'detected_face.jpg'
            cv2.imwrite(face_img_name, image)
            print(f"Face detected and saved as {face_img_name}.")
            return face_img_name
        else:
            print("No faces detected.")
            return None

def save_face_to_db(face_img_name):
    """Save the detected face image to MongoDB."""
    with open(face_img_name, 'rb') as f:
        image_data = f.read()
    insert_image(image_data)
