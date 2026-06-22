# voice/stt.py

from faster_whisper import WhisperModel

print("Loading Whisper model...")

model = WhisperModel(
    "base.en",
    device="cpu",
    compute_type="int8"
)

print("Whisper loaded successfully.")


def normalize_text(text: str) -> str:

    text = text.lower()

    replacements = {
        "suro": "zoro",
        "zorro": "zoro",
        "zero": "zoro",
        "sora": "zoro",
        "soro": "zoro",
    }

    words = text.split()

    normalized_words = [
        replacements.get(word, word)
        for word in words
    ]

    return " ".join(normalized_words)


def transcribe(audio_file):

    segments, _ = model.transcribe(
        audio_file,
        language="en",
        beam_size=3,
        vad_filter=True
    )

    text = ""

    for segment in segments:
        text += segment.text + " "

    text = text.strip()

    text = normalize_text(text)

    return text