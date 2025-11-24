import string

alphabet = string.ascii_lowercase
reversed_alphabet = alphabet[::-1]
mapping = str.maketrans(alphabet, reversed_alphabet)


def encode(plain_text):
    # Keep only letters and digits, convert to lowercase
    cleaned = []
    for ch in plain_text.lower():
        if ch.isalnum():
            cleaned.append(ch)
    cleaned = "".join(cleaned)

    # Apply Atbash translation to letters (leave numbers unchanged)
    translated = []
    for ch in cleaned:
        if ch.isalpha():
            translated.append(ch.translate(mapping))
        else:
            translated.append(ch)
    translated = "".join(translated)

    # Group into blocks of 5
    grouped = []
    for i in range(0, len(translated), 5):
        grouped.append(translated[i:i+5])

    return " ".join(grouped)


def decode(ciphered_text):
    # Remove spaces
    cleaned = ciphered_text.replace(" ", "")

    # Apply Atbash translation to letters (leave numbers unchanged)
    translated = []
    for ch in cleaned:
        if ch.isalpha():
            translated.append(ch.translate(mapping))
        else:
            translated.append(ch)
    return "".join(translated)

