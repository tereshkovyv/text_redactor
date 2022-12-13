import os

from model.cursor import Cursor


class FilenameEditor:
    def __init__(self, is_test=False):
        if is_test:
            self.width = 10
        else:
            self.width = os.get_terminal_size().columns - 7
        self.content = [""]
        self.cursor = Cursor(self.content)

    def remove_char_backspace(self):
        if self.cursor.position.word == 0:
            return
        self.content[0] = self.content[0][:self.cursor.position.word-1] + self.content[0][self.cursor.position.word:]
        self.cursor.left()
        self.cursor.update_data(self.content)

    def remove_char_delete(self):
        if self.cursor.position.word == len(self.content[0]):
            return
        self.content[0] = self.content[0][:self.cursor.position.word] + self.content[0][self.cursor.position.word+1:]
        self.cursor.update_data(self.content)

    def add_char(self, char='f'):
        if char == '\n':
            return
        self.content[0] = self.content[0][:self.cursor.position.word + 1] + char + self.content[0][self.cursor.position.word:]

        self.cursor.update_data(self.content)
        self.cursor.right()
