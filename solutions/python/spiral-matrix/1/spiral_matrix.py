def spiral_matrix(size):
    if size == 0:
        return []

    # Initialize an empty size x size matrix filled with zeros
    matrix = [[0] * size for _ in range(size)]

    num = 1
    top, bottom = 0, size - 1
    left, right = 0, size - 1

    while top <= bottom and left <= right:

        # Traverse left → right
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1

        # Traverse top → bottom
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            # Traverse right → left
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

        if left <= right:
            # Traverse bottom → top
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

    return matrix
