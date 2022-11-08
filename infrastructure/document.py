from infrastructure.position import Position


class Document:
    @property
    def data_in_lines(self):
        return self.data

    def __init__(self, path):
        self.deleted_lines = []  # int
        self.inserted_lines = []  # (int, string)
        self.changed_lines = []  # (int, string)
        self.original_content = []  # lines

        with open(path, 'r', encoding='utf-8') as f:
            self.data = f.readlines()

            for line in self.data:
                self.original_content += line

    def add_char(self, position, char):
        self.data[position.line] = self.data[position.line][:position.word] + char + self.data[position.line][position.word:]

    def del_char(self, position):
        if len(self.data[position.line]) == 1:
            del self.data[position.line]
            return
        self.data[position.line] = self.data[position.line][:position.word] + self.data[position.line][position.word+1:]

    def backspace_char(self, position):
        if len(self.data[position.line]) == 1:
            del self.data[position.line]
            return
        self.data[position.line] = self.data[position.line][:position.word-1] + self.data[position.line][position.word:]

    def save(self):
        pass
