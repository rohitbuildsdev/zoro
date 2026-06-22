def normalize_text(text: str) -> str:

    text = text.lower()

    replacements = {
        "suro": "zoro",
        "zorro": "zoro",
        "zero": "zoro",
        "sora": "zoro",
        "soro": "zoro"
    }

    words = text.split()

    normalized = [
        replacements.get(word, word)
        for word in words
    ]

    return " ".join(normalized)