BLACK = "B"
WHITE = "W"
NONE = ""


class Board:
    """Count territories of each player in a Go game"""

    def __init__(self, board):
        self.board = board
        self.height = len(board)
        self.width = len(board[0]) if self.height > 0 else 0

    def _in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def _neighbors(self, x, y):
        return [(nx, ny) for nx, ny in
                ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
                if self._in_bounds(nx, ny)]

    def territory(self, x, y):
        """Return owner + territory set at given coordinate"""

        if not self._in_bounds(x, y):
            raise ValueError("Invalid coordinate")

        stone = self.board[y][x]

        # Stones do not define a territory → None owner + empty territory
        if stone in (BLACK, WHITE):
            return (NONE, set())

        # If not empty, not a valid territory location
        if stone != " ":
            return (NONE, set())

        territory = set()
        visited = set()
        owner_candidates = set()

        queue = [(x, y)]

        while queue:
            cx, cy = queue.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))

            char = self.board[cy][cx]

            if char == " ":
                territory.add((cx, cy))
                for nx, ny in self._neighbors(cx, cy):
                    queue.append((nx, ny))
            elif char in (BLACK, WHITE):
                owner_candidates.add(char)

        # Determine territory ownership
        if len(owner_candidates) == 1:
            owner = owner_candidates.pop()
        else:
            owner = NONE

        return (owner, territory)

    def territories(self):
        """Return dict mapping owner -> set of coordinates"""
        results = {BLACK: set(), WHITE: set(), NONE: set()}
        visited = set()

        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in visited:
                    continue

                if self.board[y][x] == " ":
                    owner, terr = self.territory(x, y)
                    results[owner] |= terr
                    visited |= terr
                else:
                    visited.add((x, y))

        return results
