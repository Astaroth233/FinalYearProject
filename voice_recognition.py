import sounddevice as sd
import numpy as np
import wavio
from database import insert_image  # Use for saving audio if required
from Crypto.Cipher import AES
import os
import base64

def capture_voice(filename='captured_voice.wav', duration=5):
    """Capture audio from the microphone."""
    print("Recording...")
    audio = sd.rec(int(duration * 44100), samplerate=44100, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished
    wavio.write(filename, audio, 44100, sampwidth=2)
    print(f"Voice saved as {filename}")
    return filename

def encrypt_voice(voice_file, output_file):
    """Encrypt the captured voice file."""
    key = os.urandom(16)  # AES requires a key of 16, 24, or 32 bytes
    cipher = AES.new(key, AES.MODE_EAX)
    
    with open(voice_file, 'rb') as file:
        plaintext = file.read()
    
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # Save the encrypted file
    with open(output_file, 'wb') as enc_file:
        enc_file.write(cipher.nonce + tag + ciphertext)

    print(f"Voice file encrypted and saved as {output_file}.")