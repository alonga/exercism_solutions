# Globals for the directions
EAST = 1
NORTH = 2
WEST = 3
SOUTH = 4


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x = x_pos
        self.y = y_pos

    @property
    def coordinates(self):
        return (self.x, self.y)

    def move(self, instructions):
        for action in instructions:
            if action == "R":
                self.turn_right()
            elif action == "L":
                self.turn_left()
            elif action == "A":
                self.advance()
        return self

    def turn_right(self):
        # Rotate clockwise: North → East → South → West → North
        rotate = {NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH}
        self.direction = rotate[self.direction]

    def turn_left(self):
        # Rotate counter-clockwise: North → West → South → East → North
        rotate = {NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH}
        self.direction = rotate[self.direction]

    def advance(self):
        if self.direction == NORTH:
            self.y += 1
        elif self.direction == SOUTH:
            self.y -= 1
        elif self.direction == EAST:
            self.x += 1
        elif self.direction == WEST:
            self.x -= 1
