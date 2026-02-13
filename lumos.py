import sounddevice as sd
import numpy as np
import speech_recognition as sr
import serial
import time
from scipy.io.wavfile import write
import tempfile

# CHANGE COM PORT
arduino = serial.Serial("COM3", 9600)
time.sleep(2)

recognizer = sr.Recognizer()

samplerate = 16000
duration = 3  # seconds

print("Voice control ready...")

while True:
    print("Say command:")
    
    # Record audio
    recording = sd.rec(int(duration * samplerate),
                       samplerate=samplerate,
                       channels=1,
                       dtype='int16')
    sd.wait()

    # Save temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        write(f.name, samplerate, recording)
        filename = f.name

    # Recognize speech
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio).lower()
        print("You said:", text)

        if "lumos" in text or "lumas" in text or "loomos" in text or "lomos" in text or "on" in text:
            arduino.write(b"ON\n")
            print("LED ON")

        elif "nox" in text or "knox" in text or "nocks" in text or "noxs" in text or "off" in text:
            arduino.write(b"OFF\n")
            print("LED OFF")
        elif "silencio" in text or "silensio" in text or "selinsio" in text or "sillencio" in text:
            print("Stopping program...")
            break

    except Exception as e:
        print("Could not understand:", e)
