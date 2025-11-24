DIGITS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white"
]

TOLERANCE = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%",
}


def resistor_label(colors):
    # One-band resistor → always 0 ohms
    if len(colors) == 1:
        return "0 ohms"

    # 4-band resistor
    if len(colors) == 4:
        digits = DIGITS.index(colors[0]) * 10 + DIGITS.index(colors[1])
        multiplier = DIGITS.index(colors[2])
        tolerance = TOLERANCE[colors[3]]

    # 5-band resistor
    else:  # len(colors) == 5
        digits = (DIGITS.index(colors[0]) * 100 +
                  DIGITS.index(colors[1]) * 10 +
                  DIGITS.index(colors[2]))
        multiplier = DIGITS.index(colors[3])
        tolerance = TOLERANCE[colors[4]]

    value = digits * (10 ** multiplier)
    return f"{_format_value(value)} {tolerance}"


def _format_value(value):
    """Format ohm values including decimal when required."""
    if value >= 1_000_000_000:
        return f"{_trim(value / 1_000_000_000)} gigaohms"
    elif value >= 1_000_000:
        return f"{_trim(value / 1_000_000)} megaohms"
    elif value >= 1_000:
        return f"{_trim(value / 1_000)} kiloohms"
    return f"{value} ohms"


def _trim(num):
    """Remove trailing zeros without losing needed decimals."""
    s = f"{num:.12g}"  # smart formatting (keeps precision, no scientific)
    return s.rstrip(".")  # clean end
