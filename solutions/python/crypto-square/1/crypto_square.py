import math
import re

def cipher_text(plain_text):
    # Normalize input: keep only lowercase letters & numbers
    text = re.sub(r'[^0-9a-z]', '', plain_text.lower())
    if not text:
        return ""

    length = len(text)
    # Compute r and c
    r = int(math.floor(math.sqrt(length)))
    c = int(math.ceil(math.sqrt(length)))
    if r * c < length:
        r += 1

    # Fill rectangle row by row
    rows = [text[i:i+c] for i in range(0, length, c)]

    # Pad last row if needed
    rows[-1] = rows[-1].ljust(c)

    # Read by columns and build output chunks
    result_chunks = []
    for col in range(c):
        chunk = ''.join(row[col] for row in rows)
        result_chunks.append(chunk)

    return " ".join(result_chunks)

