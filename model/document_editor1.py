from infrastructure.cursor import Cursor
from infrastructure.position import Position
from infrastructure.document import Document


class DocumentEditor:
    @property
    def current_char(self):
        return self.content[self.cursor.y][self.cursor.x]

    def __init__(self, document, _width, _height):
        self.width = _width
        self.height = _height
        self.document = document
        self.cursor = Cursor(self.content)
        self.modified = False

    def remove_char_backspace(self):
        pass

    def remove_char_delete(self):
        pass

    def add_char(self, char='f'):
        pass

    def original_to_editor_position(self, position):
        pos = Position(self.old_to_new_line[position.line], position.word)
        for i in range(self.old_to_new_line[position.line], len(self.old_to_new_line)):
            if len(self.content[i]) > pos.word:
                break
            pos.line += 1
            pos.word -= len(self.content[i])
        return pos

    def editor_to_original_position(self, position):
        pos = Position(position.line, position.word)
        for i in range(position.line, -1, -1):
            if i in self.old_to_new_line:
                break
            pos.line -= 1
            pos.word += len(self.content[i - 1])
        pos.line = self.old_to_new_line.index(pos.line)
        return pos

    def update_content(self, position):
        pass

    def _get_content(self, start, offset):
        pass