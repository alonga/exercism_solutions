class Queen:
    def __init__(self, row, column):
        # Validate row
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")

        # Validate column
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        # Same square
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        # Same row
        if self.row == another_queen.row:
            return True

        # Same column
        if self.column == another_queen.column:
            return True

        # Same diagonal -> absolute difference of rows = absolute difference of columns
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True

        return False
