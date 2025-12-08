from itertools import permutations


def drinks_water():
    return _solve()[0]


def owns_zebra():
    return _solve()[1]


def _solve():
    nationalities = ("Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese")
    colors = ("red", "green", "ivory", "yellow", "blue")
    pets = ("dog", "snails", "fox", "horse", "zebra")
    drinks = ("coffee", "tea", "milk", "orange juice", "water")
    hobbies = ("dancing", "painting", "reading", "football", "chess")

    for nat in permutations(nationalities):
        if nat[0] != "Norwegian":
            continue  # Clue 10

        for col in permutations(colors):
            if col[nat.index("Englishman")] != "red":
                continue  # Clue 2
            if col.index("green") != col.index("ivory") + 1:
                continue  # Clue 6
            if abs(col.index("blue") - nat.index("Norwegian")) != 1:
                continue  # Clue 15

            for dr in permutations(drinks):
                if dr[2] != "milk":
                    continue  # Clue 9
                if dr[col.index("green")] != "coffee":
                    continue  # Clue 4
                if dr[nat.index("Ukrainian")] != "tea":
                    continue  # Clue 5

                for pet in permutations(pets):
                    if pet[nat.index("Spaniard")] != "dog":
                        continue  # Clue 3

                    for hob in permutations(hobbies):
                        if hob[pet.index("snails")] != "dancing":
                            continue  # Clue 7
                        if hob[col.index("yellow")] != "painting":
                            continue  # Clue 8
                        if abs(hob.index("reading") - pet.index("fox")) != 1:
                            continue  # Clue 11
                        if abs(hob.index("painting") - pet.index("horse")) != 1:
                            continue  # Clue 12
                        if dr[hob.index("football")] != "orange juice":
                            continue  # Clue 13
                        if hob[nat.index("Japanese")] != "chess":
                            continue  # Clue 14

                        # Clue 1 implied: exactly 5 houses → unique solution
                        return nat[dr.index("water")], nat[pet.index("zebra")]

    raise Exception("No valid solution found")
