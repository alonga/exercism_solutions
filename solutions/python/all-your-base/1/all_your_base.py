def rebase(input_base, digits, output_base):
    # Validate bases
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # Validate digits list
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # Edge case: empty or zero digits → return [0]
    if not digits or all(d == 0 for d in digits):
        return [0]

    # Convert digits from input_base → base 10 (integer value)
    value = 0
    for d in digits:
        value = value * input_base + d

    # Convert base10 value → output_base digits
    result = []
    while value > 0:
        value, remainder = divmod(value, output_base)
        result.append(remainder)

    # Result was built backwards
    result.reverse()
    return result

