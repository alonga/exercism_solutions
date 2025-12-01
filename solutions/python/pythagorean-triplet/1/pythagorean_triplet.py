def triplets_with_sum(number):
    triplets = []

    # a must be at least 1, and less than number/3
    for a in range(1, number // 3):
        # b must be > a and < number/2
        for b in range(a + 1, number // 2):
            c = number - a - b  # because a + b + c = number
            if c <= b:          # must satisfy a < b < c
                continue

            if a * a + b * b == c * c:
                triplets.append([a, b, c])

    return triplets
