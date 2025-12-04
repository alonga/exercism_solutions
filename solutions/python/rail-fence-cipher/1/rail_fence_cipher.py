def _build_pattern(length, rails):
    """Return the rail index for each character position."""
    pattern = []
    rail = 0
    direction = 1  # 1 = down, -1 = up

    for _ in range(length):
        pattern.append(rail)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return pattern


def encode(message, rails):
    if rails <= 1 or len(message) <= 1:
        # With 0 or 1 rail, or very short message, nothing to transpose
        return message

    pattern = _build_pattern(len(message), rails)

    # Collect characters per rail
    fence = [''] * rails
    for ch, r in zip(message, pattern):
        fence[r] += ch

    # Read row by row
    return ''.join(fence)


def decode(encoded_message, rails):
    if rails <= 1 or len(encoded_message) <= 1:
        return encoded_message

    length = len(encoded_message)
    pattern = _build_pattern(length, rails)

    # How many characters go into each rail?
    rail_counts = [pattern.count(r) for r in range(rails)]

    # Slice the encoded text into chunks per rail
    rails_content = []
    idx = 0
    for count in rail_counts:
        rails_content.append(list(encoded_message[idx:idx + count]))
        idx += count

    # Rebuild original text by walking the pattern
    positions = [0] * rails
    result = []

    for r in pattern:
        result.append(rails_content[r][positions[r]])
        positions[r] += 1

    return ''.join(result)
