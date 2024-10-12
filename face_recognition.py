import os
import cv2
import mediapipe as mp
from database import insert_image

# Create 'data/' folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)
mp_drawing = mp.solutions.drawing_utils

def capture_image(img_name):
    # Open the webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(img_name, frame)  # Save the captured frame
        cap.release()
        return img_name
    else:
        print("Failed to capture image")
        cap.release()
        return None

def detect_face(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Image not found at {image_path}")
        return None  # Return None if the image is not loaded

    # Convert the image to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image using the face detection instance
    results = face_detection.process(rgb_image)

    # Check if any faces are detected
    if results.detections:
        for detection in results.detections:
            # Optionally draw the detection on the image (for debugging)
            mp_drawing.draw_detection(image, detection)

        # Save the image with detections
        detected_face_path = os.path.join('data', f'detected_{os.path.basename(image_path)}')
        cv2.imwrite(detected_face_path, image)
        print(f"Detected face image saved at: {detected_face_path}")  # Log the path
        return detected_face_path  # Return the path of the saved image
    else:
        print("No faces detected.")
        return None  # Return None if no faces were detected

def save_face_to_db(face_img_name):
    """Save the detected face image to MongoDB."""
    if os.path.exists(face_img_name):  # Check if the file exists
        with open(face_img_name, 'rb') as f:
            image_data = f.read()
        insert_image(image_data)
    else:
        print(f"Error: Face image not found at {face_img_name}")
