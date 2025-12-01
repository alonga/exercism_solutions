def proverb(*items, qualifier=None):
    if not items:
        return []

    lines = []

    # Main proverb lines
    for first, second in zip(items, items[1:]):
        lines.append(f"For want of a {first} the {second} was lost.")

    # Final line
    first_item = f"{qualifier} {items[0]}" if qualifier else items[0]
    lines.append(f"And all for the want of a {first_item}.")

    return lines

