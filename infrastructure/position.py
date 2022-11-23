class Position:
    line = 0
    word = 0

    def __init__(self, line, word):
        self.line = line
        self.word = word

    def __eq__(self, other):
        return self.line == other.line and self.word == other.word

    def __str__(self):
        return f'({self.line}, {self.word})'
