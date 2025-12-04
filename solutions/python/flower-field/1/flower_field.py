def annotate(garden):
    # Validate input is a list of strings
    if not isinstance(garden, list) or any(not isinstance(row, str) for row in garden):
        raise ValueError("The board is invalid with current input.")

    if not garden:
        return []

    width = len(garden[0])
    if any(len(row) != width for row in garden):
        raise ValueError("The board is invalid with current input.")

    valid_chars = {' ', '*'}
    if any(ch not in valid_chars for row in garden for ch in row):
        raise ValueError("The board is invalid with current input.")

    rows = len(garden)
    cols = width

    # All 8 possible neighbor directions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    result = []

    for r in range(rows):
        new_row = []
        for c in range(cols):
            if garden[r][c] == '*':
                new_row.append('*')
                continue

            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if garden[nr][nc] == '*':
                        count += 1

            new_row.append(str(count) if count > 0 else ' ')

        result.append("".join(new_row))

    return result

