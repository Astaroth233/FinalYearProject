from Crypto.Cipher import AES
import os
import base64

def encrypt_face(face_img):
    # Your face encryption logic here
    pass

def encrypt_voice(voice_file):
    # Example voice encryption logic
    key = os.urandom(16)  # AES requires a key of 16, 24, or 32 bytes
    cipher = AES.new(key, AES.MODE_EAX)
    
    with open(voice_file, 'rb') as file:
        plaintext = file.read()
    
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    
    return cipher.nonce, ciphertext, tag  # Return the nonce, ciphertext, and tag
