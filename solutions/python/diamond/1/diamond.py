def rows(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = alphabet.index(letter)          # distance from A
    diamond = []

    for i in range(n + 1):
        ch = alphabet[i]
        outer = n - i                   # spaces before/after letters
        if ch == 'A':
            line = " " * outer + "A" + " " * outer
        else:
            inner = 2 * i - 1           # spaces between identical letters
            line = " " * outer + ch + " " * inner + ch + " " * outer
        diamond.append(line)

    # Mirror vertically (exclude middle row once)
    bottom = diamond[:-1][::-1]
    return diamond + bottom

