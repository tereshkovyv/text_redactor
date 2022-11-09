from infrastructure.position import Position


class Document:
    @property
    def data_in_lines(self):
        return self.data

    def __init__(self, path):
        self.deleted_lines = []  # int
        self.inserted_lines = []  # (int, string)
        self.changed_lines = []  # (int, string)

        with open(path, 'r', encoding='utf-8') as f:
            self.data = f.readlines()

    def add_char(self, position, char):
        self.data[position.line] = self.data[position.line][:position.word] + char + self.data[position.line][position.word:]

    def add_new_line_char(self, position):
        temp = self.data[position.line]
        self.data[position.line] = temp[:position.word] + '\n'
        self.data.insert(position.line + 1, temp[position.word:])

    def del_char(self, position):
        if len(self.data[position.line]) == 1:
            del self.data[position.line]
            return
        if position.word == len(self.data[position.line]) - 1:
            if position.line == len(self.data) - 1:
                return
            self.data[position.line] = self.data[position.line][:-1] + self.data[position.line + 1]
            del self.data[position.line + 1]
            return
        self.data[position.line] = self.data[position.line][:position.word] + self.data[position.line][position.word+1:]

    def backspace_char(self, position):
        if position.line == 0 and position.word == 0:
            return
        if len(self.data[position.line]) == 1:
            del self.data[position.line]
            return
        if position.word == 0 and position.line != 0:
            self.data[position.line - 1] = self.data[position.line - 1][:-1] + self.data[position.line]
            del self.data[position.line]
            return
        self.data[position.line] = self.data[position.line][:position.word-1] + self.data[position.line][position.word:]

    def save(self):
        pass
