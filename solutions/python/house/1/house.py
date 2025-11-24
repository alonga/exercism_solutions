PHRASES = [
    "the house that Jack built.",
    "the malt",
    "the rat",
    "the cat",
    "the dog",
    "the cow with the crumpled horn",
    "the maiden all forlorn",
    "the man all tattered and torn",
    "the priest all shaven and shorn",
    "the rooster that crowed in the morn",
    "the farmer sowing his corn",
    "the horse and the hound and the horn",
]

ACTIONS = [
    "",
    "that lay in ",
    "that ate ",
    "that killed ",
    "that worried ",
    "that tossed ",
    "that milked ",
    "that kissed ",
    "that married ",
    "that woke ",
    "that kept ",
    "that belonged to ",
]
def recite(start_verse, end_verse):
    verses = []
    for verse in range(start_verse, end_verse + 1):
        line = f"This is {PHRASES[verse - 1]}"
        for i in range(verse - 1, 0, -1):        # build backwards
            line += " " + ACTIONS[i] + PHRASES[i - 1]
        verses.append(line)
    return verses
