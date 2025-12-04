class Matrix:
    def __init__(self, matrix_string):
        # Convert input string into a list of rows of integers
        self.rows = [
            list(map(int, row.split()))
            for row in matrix_string.splitlines()
        ]

    def row(self, index):
        # index is 1-based in tests
        return self.rows[index - 1].copy()

    def column(self, index):
        # Extract the index-th element from each row (1-based)
        return [row[index - 1] for row in self.rows]

