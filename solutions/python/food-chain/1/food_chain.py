def recite(start_verse, end_verse):
    animals = [
        "fly",
        "spider",
        "bird",
        "cat",
        "dog",
        "goat",
        "cow",
        "horse",
    ]

    second_lines = {
        "fly": "",
        "spider": "It wriggled and jiggled and tickled inside her.",
        "bird": "How absurd to swallow a bird!",
        "cat": "Imagine that, to swallow a cat!",
        "dog": "What a hog, to swallow a dog!",
        "goat": "Just opened her throat and swallowed a goat!",
        "cow": "I don't know how she swallowed a cow!",
        "horse": "She's dead, of course!",
    }

    fly_ending = "I don't know why she swallowed the fly. Perhaps she'll die."

    lines = []

    for verse in range(start_verse, end_verse + 1):
        idx = verse - 1
        animal = animals[idx]

        # First line
        lines.append(f"I know an old lady who swallowed a {animal}.")

        # Special case: horse verse ends the song
        if animal == "horse":
            lines.append(second_lines["horse"])
        else:
            # Optional second line (empty for fly)
            if second_lines[animal]:
                lines.append(second_lines[animal])

            # Cumulative "she swallowed X to catch Y" lines
            # Walk backwards from current animal down to the fly
            for i in range(idx, 0, -1):
                predator = animals[i]
                prey = animals[i - 1]
                if prey == "spider":
                    lines.append(
                        "She swallowed the "
                        f"{predator} to catch the spider that wriggled and jiggled and tickled inside her."
                    )
                else:
                    lines.append(f"She swallowed the {predator} to catch the {prey}.")

            # Final fly line
            lines.append(fly_ending)

        # Blank line between verses, but not after the last requested verse
        if verse != end_verse:
            lines.append("")

    return lines
