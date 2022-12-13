from infrastructure.position import Position
from infrastructure.cursor_hit_the_edge_exception import CursorHitTheEdgeException


class Cursor:
    x = 0
    y = 0

    @property
    def position(self):
        return Position(self.y, self.x)

    def __init__(self, data):
        self.x_limit = None
        self.y_limit = None
        self.update_data(data)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def right(self):
        if self.x < self.x_limit[self.y] - 1:
            self.x += 1
        elif self.y < self.y_limit - 1:
            self.x = 0
            self.y += 1

    def left(self):
        if self.x > 0:
            self.x -= 1
        elif self.y > 0:
            self.y -= 1
            self.x = self.x_limit[self.y] - 1

    def up(self):
        if self.y > 0:
            self.y -= 1
            self.x = min(self.x, self.x_limit[self.y] - 1)

        elif self.y == 0:
            raise CursorHitTheEdgeException()

    def down(self):
        if self.y < self.y_limit - 1:
            self.y += 1
            self.x = min(self.x, self.x_limit[self.y] - 1)

        if self.y == self.y_limit - 1:
            raise CursorHitTheEdgeException()

    def update_data(self, data):
        self.y_limit = len(data)
        self.x_limit = []
        for line in data:
            self.x_limit.append(len(line) + 1)

        if self.y_limit != 0:
            self.y = min(self.y, self.y_limit - 1)
        if len(self.x_limit) != 0 and self.x_limit[self.y] != 0:
            self.x = min(self.x, self.x_limit[self.y] - 1)
