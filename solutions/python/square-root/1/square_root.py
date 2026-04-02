def square_root(number):
    candidate = 1
    while candidate * candidate <= number:
        if candidate * candidate == number:
            return candidate
        candidate += 1