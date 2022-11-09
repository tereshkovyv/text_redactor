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
        self.content = []
        self.old_to_new_line = []
        self.document = document
        self.cursor = Cursor(self.content)
        self.modified = False

    def remove_char_backspace(self):
        self.document.backspace_char(self.editor_to_original_position(self.cursor.position))
        self.update_content(self.cursor.position)
        self.cursor.left()
        self.modified = True

    def remove_char_delete(self):
        self.document.del_char(self.editor_to_original_position(self.cursor.position))
        self.update_content(self.cursor.position)
        self.modified = True

    def add_char(self, char='f'):
        position = self.editor_to_original_position(self.cursor.position)
        if char != '\n':
            self.document.add_char(self.editor_to_original_position(position), char)
        else:
            self.document.add_new_line_char(self.editor_to_original_position(position))
        self.update_content(position)
        self.cursor.right()
        self.modified = True

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
        self.content, self.old_to_new_line = self._get_content(position.line, position.word)
        self.cursor.update_data(self.content)

    def _get_content(self, start, offset):
        final_answer = []
        current_line = ''
        old_to_new_line = []

        for line in self.document.data_in_lines[start:]:
            old_to_new_line.append(len(final_answer))
            line = line.replace(' ', '·')
            line = line.replace('\n', '¶')
            word_start = False
            word = ''

            for i in range(len(line)):
                if line[i].isalpha() and (i == 0 or not (line[i - 1].isalpha())):
                    word_start = True
                if not (line[i].isalpha()) and i > 0 and line[i - 1].isalpha() or i == len(line) - 1:
                    word_start = False
                    if len(current_line) + len(word) > self.width:
                        final_answer.append(current_line)
                        if len(final_answer) == self.height:
                            return final_answer, old_to_new_line
                        current_line = ''
                    current_line += word
                    word = ''

                if word_start:
                    word += line[i]
                else:
                    if len(current_line) > self.width - 1:
                        final_answer.append(current_line)
                        if len(final_answer) == self.height:
                            return final_answer, old_to_new_line
                        current_line = ''
                    current_line += line[i]
            final_answer.append(current_line)
            if len(final_answer) == self.height:
                return final_answer, old_to_new_line
            current_line = ''
        return final_answer, old_to_new_line
