import numpy as np
import sounddevice as sd

from openwakeword.model import Model
from config.settings import WAKEWORD_MODEL


class WakeWordDetector:

    def __init__(self):

        self.model = Model(
            wakeword_models=[WAKEWORD_MODEL]
        )

        self.sample_rate = 16000
        self.chunk_size = 1280

    def listen(self):

        print("🎤 Waiting for wake word...")

        with sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype="int16",
            blocksize=self.chunk_size
        ) as stream:

            while True:

                audio_chunk, _ = stream.read(
                    self.chunk_size
                )

                audio_chunk = (
                    audio_chunk.flatten()
                    .astype(np.int16)
                )

                prediction = self.model.predict(
                    audio_chunk
                )

                for model_name, score in prediction.items():

                    if score > 0.5:

                        print(
                            f"\nWake word detected ({score:.2f})"
                        )

                        return True