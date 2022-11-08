from infrastructure.position import Position


class Cursor:
    x = 0
    y = 0

    @property
    def position(self):
        return Position(self.y, self.x)

    @position.setter
    def position(self, new):
        x = new.line
        y = new.word

    def __init__(self, data):
        self.x_limit = None
        self.y_limit = None
        self.update_data(data)

    def right(self):
        if self.x < self.x_limit[self.y] - 1:
            self.x += 1
        elif self.y < self.y_limit:
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
            self.x = min(self.x, self.x_limit[self.y])

    def down(self):
        if self.y < self.y_limit - 1:
            self.y += 1
            self.x = min(self.x, self.x_limit[self.y])

    def update_data(self, data):
        self.y_limit = len(data)
        self.x_limit = []
        for line in data:
            self.x_limit.append(len(line))