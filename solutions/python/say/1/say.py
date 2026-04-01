def say(number):
    # Validate input
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    # Dictionaries for numbers
    ones = [
        "", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
        "nineteen"
    ]

    tens = [
        "", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]

    # Convert a number <= 999
    def under_1000(n):
        words = []

        if n >= 100:
            words.append(ones[n // 100] + " hundred")
            n %= 100
            if n:
                words.append("")  # space placeholder

        if n >= 20:
            ten_part = tens[n // 10]
            n %= 10
            if n:
                words.append(f"{ten_part}-{ones[n]}")
            else:
                words.append(ten_part)
        elif n > 0:
            words.append(ones[n])

        return " ".join(w for w in words if w)

    parts = []
    scales = [
        (1_000_000_000, "billion"),
        (1_000_000, "million"),
        (1_000, "thousand"),
        (1, "")
    ]

    for scale_value, scale_name in scales:
        if number >= scale_value:
            chunk = number // scale_value
            number %= scale_value
            segment = under_1000(chunk)
            if scale_name:
                parts.append(segment + " " + scale_name)
            else:
                parts.append(segment)

    return " ".join(parts)
