def translate(text):
    return " ".join(translate_word(word) for word in text.split())


def translate_word(word):
    vowels = ("a", "e", "i", "o", "u")

    # Rule 1 – vowel start or "xr" / "yt"
    if word.startswith(vowels) or word.startswith(("xr", "yt")):
        return word + "ay"

    # Find index of first vowel
    first_vowel = next((i for i, ch in enumerate(word) if ch in vowels), -1)

    # Rule 3 – consonants followed immediately by "qu"
    # (covers both "qu..." and "...qu..." after initial consonant cluster)
    if "qu" in word:
        qu_index = word.find("qu")
        # qu must come right after the leading consonants or at start
        if qu_index == 0 or (first_vowel != -1 and qu_index == first_vowel - 1 or qu_index == first_vowel):
            idx = qu_index + 2
            return word[idx:] + word[:idx] + "ay"

    # Rule 4 – no vowel before 'y' → treat y as the vowel
    if first_vowel == -1 and "y" in word[1:]:
        yidx = word.find("y")
        return word[yidx:] + word[:yidx] + "ay"

    # Rule 2 – normal consonant cluster until first vowel
    idx = first_vowel
    return word[idx:] + word[:idx] + "ay"
