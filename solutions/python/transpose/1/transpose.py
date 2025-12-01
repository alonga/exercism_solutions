def transpose(text):
    rows = text.split("\n")
    h = len(rows)
    # width of the longest input row
    w = max((len(r) for r in rows), default=0)

    # Build two grids:
    #   grid[r][c]  = character at row r, col c (padded with ' ')
    #   orig[r][c]  = True if that character is from the original text, False if it's padding
    grid = []
    orig = []
    for r in rows:
        line_chars = []
        line_flags = []
        for c in range(w):
            if c < len(r):
                line_chars.append(r[c])
                line_flags.append(True)   # real character from input
            else:
                line_chars.append(" ")
                line_flags.append(False)  # padding
        grid.append(line_chars)
        orig.append(line_flags)

    result_rows = []
    # Now transpose: columns become rows
    for c in range(w):
        chars = [grid[r][c] for r in range(h)]
        flags = [orig[r][c] for r in range(h)]

        # Trim trailing spaces, but only if they are *padding* (orig == False)
        i = len(chars) - 1
        while i >= 0 and chars[i] == " " and not flags[i]:
            i -= 1

        result_rows.append("".join(chars[:i + 1]))

    return "\n".join(result_rows)





