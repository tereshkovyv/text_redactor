class Document:
    def __init__(self, path):
        self.data = []
        self.iteration_index = -1
        self.path = path
        self.file = open(self.path, 'r', encoding='utf-8')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        self.iteration_index += 1
        while self.iteration_index >= len(self.data):
            self.data.append(self.file.__next__())
        return self.data[self.iteration_index]

    def data_in_lines(self, start):
        self.iteration_index = start-1
        return self

    def add_common_char(self, position, char):
        self.data[position.line] = self.data[position.line][:position.word] + char + self.data[position.line][position.word:]

    def add_new_line_char(self, position):
        temp = self.data[position.line]
        self.data[position.line] = temp[:position.word] + '\n'
        self.data.insert(position.line + 1, temp[position.word:])

    def delete_char(self, position):
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
        for _ in self:
            pass
        self.file.close()
        with open(self.path, 'w', encoding='utf-8') as file:
            for line in self.data:
                file.write(line)
