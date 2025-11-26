import re

def abbreviate(words):
    # Replace hyphens with spaces so they are treated as separators
    cleaned = words.replace('-', ' ')
    # Remove all punctuation except spaces and letters
    cleaned = re.sub(r"[^A-Za-z\s]", "", cleaned)
    # Split into words
    parts = cleaned.split()
    # Take first character of each word, uppercase, and build acronym
    return ''.join(word[0].upper() for word in parts)
