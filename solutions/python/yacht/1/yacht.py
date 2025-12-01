# Score categories.
YACHT = "yacht"
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "four_kind"
LITTLE_STRAIGHT = "little_straight"
BIG_STRAIGHT = "big_straight"
CHOICE = "choice"


def score(dice, category):
    counts = {x: dice.count(x) for x in range(1, 7)}

    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return category * counts.get(category, 0)

    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0

    if category == FULL_HOUSE:
        # sorted values of counts must be [2, 3]
        if sorted(counts.values(), reverse=True)[:2] == [3, 2]:
            return sum(dice)
        return 0

    if category == FOUR_OF_A_KIND:
        for num, cnt in counts.items():
            if cnt >= 4:
                return num * 4
        return 0

    if category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0

    if category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0

    if category == CHOICE:
        return sum(dice)

    return 0
