def flatten(iterable):
    result = []

    for item in iterable:
        if isinstance(item, list):           # nested list → recurse
            result.extend(flatten(item))
        elif item is not None:               # ignore null-like values
            result.append(item)

    return result

