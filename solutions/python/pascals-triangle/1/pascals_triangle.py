def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")

    if row_count == 0:
        return []

    if row_count == 1:
        return [[1]]

    # Recursively build the triangle up to previous row
    triangle = rows(row_count - 1)
    prev = triangle[-1]

    # Build the next row recursively from previous
    new_row = [1]
    for i in range(len(prev) - 1):
        new_row.append(prev[i] + prev[i + 1])
    new_row.append(1)

    triangle.append(new_row)
    return triangle
