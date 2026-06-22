# voice/tts.py

import pyttsx3


def speak(text):

    text = str(text)

    print(f"\nZORO: {text}")

    engine = pyttsx3.init()

    engine.setProperty("rate", 220)
    engine.setProperty("volume", 1.0)

    engine.say(text)

    engine.runAndWait()

    engine.stop()