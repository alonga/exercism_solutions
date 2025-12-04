def encode(numbers):
    if not numbers:
        return []

    result = []
    for n in numbers:
        if n < 0 or n > 0xFFFFFFFF:
            raise ValueError("only 32-bit unsigned integers allowed")

        if n == 0:
            result.append(0)
            continue

        bytes_for_num = []
        while n > 0:
            bytes_for_num.append(n & 0x7F)
            n >>= 7

        # Set continuation bit on all but last byte
        for i in range(len(bytes_for_num) - 1):
            result.append(0x80 | bytes_for_num[-(i + 1)])

        # Last byte → MSB = 0
        result.append(bytes_for_num[0])

    return result


def decode(bytes_):
    if not bytes_:
        return []

    numbers = []
    current = 0
    expecting_more = False

    for b in bytes_:
        current = (current << 7) | (b & 0x7F)

        if b & 0x80:   # Continuation bit ON
            expecting_more = True
        else:          # End of number
            numbers.append(current)
            current = 0
            expecting_more = False

    if expecting_more:
        raise ValueError("incomplete sequence")

    return numbers
