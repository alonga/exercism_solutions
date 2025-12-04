def rectangles(strings):
    # Handle empty input
    if not strings:
        return 0
    
    grid = [list(row) for row in strings]
    rows = len(grid)
    cols = len(grid[0])

    def is_horiz_edge(r, c1, c2):
        return all(ch in '+-' for ch in grid[r][c1:c2 + 1])

    def is_vert_edge(r1, r2, c):
        return all(grid[r][c] in '+|' for r in range(r1, r2 + 1))

    pluses = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == '+']
    count = 0

    for r1, c1 in pluses:
        for r1b, c2 in pluses:
            if r1 == r1b and c2 > c1:
                if not is_horiz_edge(r1, c1, c2):
                    continue

                for r2 in range(r1 + 1, rows):
                    if grid[r2][c1] == '+' and grid[r2][c2] == '+':
                        if not is_horiz_edge(r2, c1, c2):
                            continue
                        if is_vert_edge(r1, r2, c1) and is_vert_edge(r1, r2, c2):
                            count += 1

    return count
