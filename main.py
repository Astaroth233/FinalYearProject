from face_recognition import capture_image, detect_face, save_face_to_db
from voice_recognition import capture_voice, encrypt_voice

def main():
    # Capture face image
    img_name = capture_image()
    face_img = detect_face(img_name)
    
    if face_img:
        save_face_to_db(face_img)  # Save the detected face image to MongoDB
    
    # Capture voice
    voice_file = capture_voice()
    encrypt_voice(voice_file)  # Encrypt the voice file

if __name__ == "__main__":
    main()  # Ensure this line is present to call the main function
