from infrastructure.cursor import Cursor
from infrastructure.position import Position
from infrastructure.document import Document


class DocumentEditor:
    @property
    def current_char(self):
        return self.content[self.cursor.y][self.cursor.x]

    def __init__(self, path, _width, _height):
        self.width = _width
        self.height = _height
        self.content = []
        self.old_to_new_line = []
        self.document = Document(path)
        self.cursor = Cursor(self.content)
        self.modified = False

    def remove_char_backspace(self):
        self.document.backspace_char(self.editor_to_original_position(self.cursor.position))
        self.cursor.left()
        self.update_content(self.cursor.position)
        self.modified = True

    def remove_char_delete(self):
        self.document.del_char(self.editor_to_original_position(self.cursor.position))
        self.update_content(self.cursor.position)
        self.modified = True

    def add_char(self, char='f'):
        self.document.add_char(self.editor_to_original_position(self.cursor.position), char)
        self.cursor.right()
        self.update_content(self.cursor.position)
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
        answer = ''
        old_to_new_line = []

        for line in self.document.data_in_lines[start:]:
            old_to_new_line.append(len(final_answer))
            line = line.replace(' ', '·')
            line = line.replace('\n', '¶')
            word_start = False
            word = ''

            for i in range(offset, len(line)):
                if line[i].isalpha() and (i == 0 or not (line[i - 1].isalpha())):
                    word_start = True
                if not (line[i].isalpha()) and i > 0 and line[i - 1].isalpha():
                    word_start = False
                    if len(answer) + len(word) > self.width:
                        final_answer.append(answer)
                        if len(final_answer) == self.height:
                            return final_answer, old_to_new_line
                        answer = ''
                    answer += word
                    word = ''

                if word_start:
                    word += line[i]
                else:
                    if len(answer) + 1 > self.width:
                        final_answer.append(answer)
                        if len(final_answer) == self.height:
                            return final_answer, old_to_new_line
                        answer = ''
                    answer += line[i]
            final_answer.append(answer)
            if len(final_answer) == self.height:
                return final_answer, old_to_new_line
            answer = ''
        return final_answer, old_to_new_line
