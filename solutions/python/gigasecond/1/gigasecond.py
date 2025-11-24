from datetime import timedelta


def add(moment):
    """Return the moment one gigasecond (1_000_000_000 seconds) later."""
    return moment + timedelta(seconds=1_000_000_000)

