import sounddevice as sd
import numpy as np
import wavio
from database import insert_image  # Use for saving audio if required

def capture_voice(filename='captured_voice.wav', duration=5):
    """Capture audio from the microphone."""
    print("Recording...")
    audio = sd.rec(int(duration * 44100), samplerate=44100, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished
    wavio.write(filename, audio, 44100, sampwidth=2)
    print(f"Voice saved as {filename}")
    return filename

def encrypt_voice(filename):
    """Encrypt the captured voice file."""
    # Implement your AES encryption here
    print(f"Encrypting voice file {filename}.")
    # Return some value (e.g., path, success flag)
