def recite(start, take=1):
    numbers = [
        "no", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine", "ten"
    ]

    def bottles(n, capitalize=False):
        word = numbers[n]
        if capitalize:
            word = word.capitalize()
        return f"{word} green bottle{'s' if n != 1 else ''}"

    verses = []
    
    for n in range(start, start - take, -1):
        verses.append(f"{bottles(n, True)} hanging on the wall,")
        verses.append(f"{bottles(n, True)} hanging on the wall,")
        verses.append("And if one green bottle should accidentally fall,")
        verses.append(f"There'll be {bottles(n - 1)} hanging on the wall.")
        
        # Blank line between verses, but not after the last verse
        if n != start - take + 1:
            verses.append("")

    return verses

