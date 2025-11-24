def find_anagrams(word, candidates):
    result = []
    w = word.lower()
    sorted_w = sorted(w)

    for candidate in candidates:
        c = candidate.lower()
        if c == w:
            continue  # skip identical word
        if sorted(c) == sorted_w:
            result.append(candidate)
    return result
