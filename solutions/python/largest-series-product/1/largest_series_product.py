def largest_product(series, size):
    # --- Validation checks in the required order ---
    if size < 0:
        raise ValueError("span must not be negative")

    if size > len(series):
        raise ValueError("span must not exceed string length")

    if any(ch not in "0123456789" for ch in series):
        raise ValueError("digits input must only contain digits")

    if size == 0:
        return 1  # convention: product of empty series = 1

    max_product = 0

    for i in range(len(series) - size + 1):
        window = series[i:i + size]
        product = 1
        for d in window:
            product *= int(d)
        if product > max_product:
            max_product = product

    return max_product

