def sum_of_multiples(limit, multiples):
    result = set()

    for m in multiples:
        if m == 0:
            continue
        for num in range(m, limit, m):
            result.add(num)

    return sum(result)
