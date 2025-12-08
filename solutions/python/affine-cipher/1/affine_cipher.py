from math import gcd
import string

ALPHABET = string.ascii_lowercase
M = 26  # length of alphabet


def encode(plain_text, a, b):
    if gcd(a, M) != 1:
        raise ValueError("a and m must be coprime.")

    result = []
    plain_text = "".join(ch.lower() for ch in plain_text if ch.isalnum())  # keep letters & digits only

    for ch in plain_text:
        if ch.isdigit():
            result.append(ch)
        else:
            i = ALPHABET.index(ch)
            encoded_val = (a * i + b) % M
            result.append(ALPHABET[encoded_val])

    # group into blocks of 5
    grouped = ["".join(result[i:i + 5]) for i in range(0, len(result), 5)]
    return " ".join(grouped)


def decode(ciphered_text, a, b):
    if gcd(a, M) != 1:
        raise ValueError("a and m must be coprime.")

    # Find modular multiplicative inverse of a mod 26
    a_inv = None
    for x in range(M):
        if (a * x) % M == 1:
            a_inv = x
            break

    ciphered_text = "".join(ch.lower() for ch in ciphered_text if ch.isalnum())

    result = []
    for ch in ciphered_text:
        if ch.isdigit():
            result.append(ch)
        else:
            y = ALPHABET.index(ch)
            decoded_val = (a_inv * (y - b)) % M
            result.append(ALPHABET[decoded_val])

    return "".join(result)
