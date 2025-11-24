COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors: list[str]) -> int:
    """Return the resistor value for the first two colors."""
    first = COLORS.index(colors[0])
    second = COLORS.index(colors[1])
    return int(f"{first}{second}")
