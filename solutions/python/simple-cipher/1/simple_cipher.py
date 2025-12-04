import string
import random

class Cipher:
    def __init__(self, key=None):
        if key is None:
            # Generate random lowercase key of length >= 100
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        else:
            # Validate: key must be only lowercase alphabetic
            if not key.isalpha() or not key.islower():
                raise ValueError("Key must be lowercase alphabetic characters")
            self.key = key

    def encode(self, text):
        return self._translate(text, encode=True)

    def decode(self, text):
        return self._translate(text, encode=False)

    def _translate(self, text, encode=True):
        result = []
        for i, ch in enumerate(text):
            shift = ord(self.key[i % len(self.key)]) - ord('a')
            if not encode:
                shift = -shift
            rotated = (ord(ch) - ord('a') + shift) % 26 + ord('a')
            result.append(chr(rotated))
        return "".join(result)

