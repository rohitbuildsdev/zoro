# core/orchestrator.py

import os
import re

import sounddevice as sd
from scipy.io.wavfile import write

from config.settings import (
    RECORD_SECONDS,
    SAMPLE_RATE,
    TEMP_AUDIO_FILE
)

from voice.stt import transcribe
from voice.tts import speak

from core.intent_parser import parse
from core.router import Router


WAKE_WORDS = [
    "zoro",
    "jarvis",
    "hey zoro",
    "hey jarvis"
]


class Orchestrator:

    def __init__(self):

        self.router = Router()

        os.makedirs(
            "recordings",
            exist_ok=True
        )

    def record_audio(self):

        print("\n🎤 Listening...")

        recording = sd.rec(
            int(RECORD_SECONDS * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        write(
            TEMP_AUDIO_FILE,
            SAMPLE_RATE,
            recording
        )

        return TEMP_AUDIO_FILE

    def detect_wake_word(self, text):

        text = text.lower()

        text = re.sub(
            r"[^\w\s]",
            "",
            text
        )

        for wake_word in WAKE_WORDS:

            if wake_word in text:

                command = text.replace(
                    wake_word,
                    "",
                    1
                ).strip()

                return True, command

        return False, ""

    def process_command(self, command):

        print(f"\nCOMMAND: {command}")

        intent_data = parse(command)

        print(
            f"\nINTENT: {intent_data}"
        )

        response = self.router.route(
            intent_data
        )

        return response

    def run(self):

        speak("Zoro initialized.")

        while True:

            audio_file = self.record_audio()

            text = transcribe(audio_file)

            print(f"\nUSER: {text}")

            wake_detected, command = (
                self.detect_wake_word(text)
            )

            if not wake_detected:

                print(
                    "\n❌ Wake word not detected"
                )

                speak(
                    "Wake word not detected."
                )

                continue

            print(
                "\n✅ Wake word detected"
            )

            if not command:

                speak(
                    "Command not detected."
                )

                continue

            response = self.process_command(
                command
            )

            print("DEBUG RESPONSE:", response)

            if response == "SHUTDOWN":

                speak(
                    "Shutting down Zoro."
                )

                break

            speak(response)