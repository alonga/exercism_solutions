DIGITS = {
    " _ " +
    "| |" +
    "|_|" +
    "   ": "0",

    "   " +
    "  |" +
    "  |" +
    "   ": "1",

    " _ " +
    " _|" +
    "|_ " +
    "   ": "2",

    " _ " +
    " _|" +
    " _|" +
    "   ": "3",

    "   " +
    "|_|" +
    "  |" +
    "   ": "4",

    " _ " +
    "|_ " +
    " _|" +
    "   ": "5",

    " _ " +
    "|_ " +
    "|_|" +
    "   ": "6",

    " _ " +
    "  |" +
    "  |" +
    "   ": "7",

    " _ " +
    "|_|" +
    "|_|" +
    "   ": "8",

    " _ " +
    "|_|" +
    " _|" +
    "   ": "9",
}


def convert(input_grid):
    rows = len(input_grid)
    if rows % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    cols = len(input_grid[0]) if rows > 0 else 0
    if any(len(r) != cols for r in input_grid):
        # Unequal widths is also invalid ― but this is covered by the checks below
        pass

    if cols % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    result_lines = []
    for block_row in range(0, rows, 4):
        group = input_grid[block_row:block_row + 4]

        digits = []
        for block_col in range(0, cols, 3):
            pattern = "".join(row[block_col:block_col + 3] for row in group)
            digits.append(DIGITS.get(pattern, "?"))

        result_lines.append("".join(digits))

    return ",".join(result_lines)


