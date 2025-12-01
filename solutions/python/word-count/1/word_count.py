import re

def count_words(sentence):
    # Normalize case
    s = sentence.lower()

    # Regex explanation:
    #   [a-z0-9]+(?:'[a-z0-9]+)?  → words and contractions (e.g. don't, i'm, he's, can't)
    #   matches:
    #      abc
    #      abc123
    #      abc'def
    #      123
    words = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", s)

    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1

    return result

