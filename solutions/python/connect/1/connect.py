
class ConnectGame:
    def __init__(self, board):
        # Allow either a single string with newlines or a list of strings
        if isinstance(board, str):
            raw_rows = board.splitlines()
        else:
            raw_rows = list(board)

        # Remove spaces from each row (Exercism's board has leading spaces)
        self.board = [row.replace(" ", "") for row in raw_rows if row.strip() != ""]
        self.rows = len(self.board)
        self.cols = len(self.board[0]) if self.rows > 0 else 0

        # Hex grid neighbors in this representation:
        # (row, col) offsets for the 6 adjacent cells
        self.dirs = [
            (-1, 0),  # up
            (-1, 1),  # up-right
            (0, -1),  # left
            (0, 1),   # right
            (1, -1),  # down-left
            (1, 0),   # down
        ]

    def get_winner(self):
        # No cells -> no winner
        if self.rows == 0 or self.cols == 0:
            return ""

        if self._has_path('X'):
            return 'X'
        if self._has_path('O'):
            return 'O'
        return ""

    def _inside(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def _has_path(self, player):
        from collections import deque

        visited = set()
        queue = deque()

        if player == 'X':
            # X connects left → right.
            # Start from all X stones in the leftmost column (col = 0).
            for r in range(self.rows):
                if self.board[r][0] == 'X':
                    queue.append((r, 0))
                    visited.add((r, 0))

            target_col = self.cols - 1

            while queue:
                r, c = queue.popleft()
                if c == target_col:
                    return True

                for dr, dc in self.dirs:
                    nr, nc = r + dr, c + dc
                    if self._inside(nr, nc) and (nr, nc) not in visited:
                        if self.board[nr][nc] == 'X':
                            visited.add((nr, nc))
                            queue.append((nr, nc))

        elif player == 'O':
            # O connects top → bottom.
            # Start from all O stones in the top row (row = 0).
            for c in range(self.cols):
                if self.board[0][c] == 'O':
                    queue.append((0, c))
                    visited.add((0, c))

            target_row = self.rows - 1

            while queue:
                r, c = queue.popleft()
                if r == target_row:
                    return True

                for dr, dc in self.dirs:
                    nr, nc = r + dr, c + dc
                    if self._inside(nr, nc) and (nr, nc) not in visited:
                        if self.board[nr][nc] == 'O':
                            visited.add((nr, nc))
                            queue.append((nr, nc))

        return False

       

