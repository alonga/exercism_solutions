def score(word):
    if not word:
        return 0

    scores = {
        **dict.fromkeys("AEIOULNRST", 1),
        **dict.fromkeys("DG", 2),
        **dict.fromkeys("BCMP", 3),
        **dict.fromkeys("FHVWY", 4),
        **dict.fromkeys("K", 5),
        **dict.fromkeys("JX", 8),
        **dict.fromkeys("QZ", 10),
    }

    total = 0
    for letter in word.upper():
        total += scores.get(letter, 0)

    return total

