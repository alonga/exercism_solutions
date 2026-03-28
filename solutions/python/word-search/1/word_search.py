class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class WordSearch:
    def __init__(self, puzzle):
        self.grid = [list(row) for row in puzzle]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if self.rows else 0

    def search(self, word):
        directions = [
            (0, 1),   # right
            (0, -1),  # left
            (1, 0),   # down
            (-1, 0),  # up
            (1, 1),   # diagonal down-right
            (1, -1),  # diagonal down-left
            (-1, 1),  # diagonal up-right
            (-1, -1)  # diagonal up-left
        ]

        for y in range(self.rows):
            for x in range(self.cols):
                if self.grid[y][x] != word[0]:
                    continue

                for dy, dx in directions:
                    if self._match(word, x, y, dx, dy):
                        end_x = x + dx * (len(word) - 1)
                        end_y = y + dy * (len(word) - 1)
                        return Point(x, y), Point(end_x, end_y)

        return None

    def _match(self, word, x, y, dx, dy):
        for i, letter in enumerate(word):
            cx = x + dx * i
            cy = y + dy * i
            if not (0 <= cx < self.cols and 0 <= cy < self.rows):
                return False
            if self.grid[cy][cx] != letter:
                return False
        return True
