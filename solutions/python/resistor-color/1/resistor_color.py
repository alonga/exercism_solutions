# Ordered list of resistor colors
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


def color_code(color: str) -> int:
    """Return the numeric code associated with a resistor color."""
    return COLORS.index(color)


def colors() -> list[str]:
    """Return the list of all resistor colors in order."""
    return COLORS.copy()

