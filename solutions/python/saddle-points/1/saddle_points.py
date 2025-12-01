def saddle_points(matrix):
    # Empty matrix → no saddle points
    if matrix == []:
        return []

    # Check for irregular matrix: all rows must have the same length
    row_lengths = {len(row) for row in matrix}
    if len(row_lengths) > 1:
        raise ValueError("irregular matrix")

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # No columns → no saddle points
    if cols == 0:
        return []

    # Precompute max of each row
    row_max = [max(row) for row in matrix]
    # Precompute min of each column
    col_min = [min(matrix[r][c] for r in range(rows)) for c in range(cols)]

    result = []
    for r in range(rows):
        for c in range(cols):
            value = matrix[r][c]
            if value == row_max[r] and value == col_min[c]:
                # Exercism expects 1-based indices and dicts
                result.append({"row": r + 1, "column": c + 1})

    return result


