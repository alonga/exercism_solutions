"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    # Case 1: exact match
    if list_one == list_two:
        return EQUAL

    # Helper to check contiguous sub-sequence
    def is_sublist(smaller, bigger):
        n, m = len(smaller), len(bigger)
        if n == 0:               # empty list is always sublist
            return True
        for i in range(m - n + 1):
            if bigger[i:i+n] == smaller:
                return True
        return False

    # Case 2: list_one inside list_two
    if is_sublist(list_one, list_two):
        return SUBLIST

    # Case 3: list_two inside list_one
    if is_sublist(list_two, list_one):
        return SUPERLIST

    # Case 4: none of the above
    return UNEQUAL
