from flask import Flask, render_template, request, redirect, url_for
from face_recognition import capture_image, detect_face, save_face_to_db
from voice_recognition import capture_voice, encrypt_voice
import os

app = Flask(__name__)

# Define paths for data storage
DATA_FOLDER = 'data/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    img_name = os.path.join(DATA_FOLDER, 'captured_face.jpg')
    face_img_name = os.path.join(DATA_FOLDER, 'detected_face.jpg')

    img_name = capture_image(img_name)  # Capture face image

    if img_name is None:
        return "Failed to capture image. Please try again."

    face_img = detect_face(img_name)  # Attempt to detect face

    if face_img is not None:
        save_face_to_db(face_img_name)  # Save the detected face image to MongoDB
        
        # Capture and encrypt voice
        voice_file = os.path.join(DATA_FOLDER, 'captured_voice.wav')
        encrypted_voice_file = os.path.join(DATA_FOLDER, 'encrypted_voice.enc')
        
        voice_file = capture_voice(voice_file)
        encrypt_voice(voice_file, encrypted_voice_file)  # Encrypt the voice file
        
        return "Recognition and Encryption Successful!"
    else:
        return "No face detected. Please try again."


if __name__ == "__main__":
    app.run(debug=True)
