from itertools import combinations as it_combinations

def combinations(target, size, exclude):
    exclude = set(exclude)

    valid = []
    for combo in it_combinations(range(1, 10), size):
        if set(combo).isdisjoint(exclude) and sum(combo) == target:
            valid.append(list(combo))

    return sorted(valid)

