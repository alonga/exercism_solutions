def rotate(text, key):
    result = []

    for char in text:
        # Rotate uppercase A–Z
        if 'A' <= char <= 'Z':
            rotated = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            result.append(rotated)
        # Rotate lowercase a–z
        elif 'a' <= char <= 'z':
            rotated = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            result.append(rotated)
        # Non-alphabetic characters remain unchanged
        else:
            result.append(char)

    return ''.join(result)
