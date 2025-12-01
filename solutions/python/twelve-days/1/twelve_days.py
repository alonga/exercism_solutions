def recite(start_verse, end_verse):
    ordinals = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]

    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
    ]

    verses = []

    for verse in range(start_verse, end_verse + 1):
        line = f"On the {ordinals[verse - 1]} day of Christmas my true love gave to me: "

        # build gift list backward
        parts = []
        for i in range(verse - 1, -1, -1):
            parts.append(gifts[i])

        # add "and" before the last gift if verse > 1
        if verse > 1:
            parts[-1] = "and " + parts[-1]

        line += ", ".join(parts)
        verses.append(line)

    return verses

