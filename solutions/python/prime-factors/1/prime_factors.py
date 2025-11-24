def factors(value):
    result = []
    divisor = 2

    while value > 1:
        while value % divisor == 0:
            result.append(divisor)
            value //= divisor
        divisor += 1

    return result
