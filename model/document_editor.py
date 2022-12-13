import re

from model.cursor import Cursor
from infrastructure.position import Position
from plugins.autocomplete.autocompleter import Autocompleter


class DocumentEditor:
    def __init__(self, document, _width, _height, disable_autocompleter=False):
        self.width = _width
        self.height = _height
        self.content = []
        self.new_to_old_line = [Position(0, 0)]
        self.document = document
        self.cursor = Cursor(self.content)
        if not disable_autocompleter:
            self.autocompleter = Autocompleter()
        else:
            self.autocompleter = None
        self.modified = False

        self.reached_end_of_file = False
        self._starting_line = 0

    def line_up(self):
        if self._starting_line > 0:
            self._starting_line -= 1
            self.update_content()

    def line_down(self):
        if not self.reached_end_of_file:
            self._starting_line += 1
            self.update_content()

    def remove_char_backspace(self):
        position = self._editor_to_original_position(self.cursor.position)
        self.document.backspace_char(position)
        self.update_content()
        self.cursor.update_data(self.content)
        self.cursor.left()
        self.modified = True

    def remove_char_delete(self):
        position = self._editor_to_original_position(self.cursor.position)
        self.document.delete_char(position)
        self.update_content()
        self.cursor.update_data(self.content)
        self.modified = True

    def add_char(self, char='f'):
        position = self._editor_to_original_position(self.cursor.position)
        if char != '\n':
            self.document.add_common_char(position, char)
        else:
            self.document.add_new_line_char(position)
        self.update_content()
        self.cursor.update_data(self.content)
        self.cursor.right()
        self.modified = True

    def _editor_to_original_position(self, position):
        return Position(self.new_to_old_line[position.line + self._starting_line].line,
                        self.new_to_old_line[position.line + self._starting_line].word + position.word)

    def update_content(self):
        self.content, _ = self._get_content()
        self.cursor.update_data(self.content)

    def _get_content(self):
        self.reached_end_of_file = False
        current_position = self.new_to_old_line[self._starting_line]
        self.new_to_old_line = self.new_to_old_line[:self._starting_line]

        current_line = ""
        answer_lines = []
        is_first_line = True
        for line in self.document.data_in_lines(current_position.line):
            line = line.replace('\n', '')

            current_word = ""
            word_start_position = Position(0, 0)
            word_started = False

            current_range = range(len(line))
            if is_first_line:
                current_range = range(current_position.word, len(line))
                is_first_line = False
            for i in current_range:
                if line[i].isalpha():
                    if word_started:
                        current_word += line[i]
                    else:
                        word_started = True
                        word_start_position = Position(current_position.line, i)
                        current_word += line[i]
                else:
                    if word_started:
                        word_started = False
                        if len(current_line) + len(current_word) > self.width:
                            answer_lines.append(current_line)
                            self.new_to_old_line.append(current_position)
                            current_position = word_start_position
                            current_line = ""
                            if len(answer_lines) == self.height:
                                self.content = answer_lines
                                return answer_lines, self.new_to_old_line

                        current_line += current_word
                        current_word = ""
                    else:
                        if len(current_line) + 1 > self.width:
                            answer_lines.append(current_line)
                            self.new_to_old_line.append(current_position)
                            current_position = Position(current_position.line, i)
                            current_line = ""
                            if len(answer_lines) == self.height:
                                self.content = answer_lines
                                return answer_lines, self.new_to_old_line

                    current_line += line[i]

            current_line += current_word
            answer_lines.append(current_line)
            self.new_to_old_line.append(current_position)
            current_position = Position(current_position.line + 1, 0)
            current_line = ""
            if len(answer_lines) == self.height:
                self.content = answer_lines
                return answer_lines, self.new_to_old_line

        self.reached_end_of_file = True
        return answer_lines, self.new_to_old_line

    def autocomplete_word(self):
        if self.cursor.position.word == 0 or len(self.content[self.cursor.position.line]) == self.cursor.position.word or self.content[self.cursor.position.line][self.cursor.position.word - 1] == ' ':
            next_word = self.autocompleter.get_next_by_previous_words(self.get_previous_word())
            print(f'ищем по предыдущим ({self.get_previous_word()}), нашли {next_word}')
        else:
            next_word = self.autocompleter.get_next_by_prefix(self.get_prefix())
            print(f'ищем по префиксу ({self.get_prefix()}) нашли: {next_word}')

        print(f'next word is: {next_word}')
        for c in str(' ' + next_word):
            self.add_char(c)

    def get_previous_word(self):
        line = self.content[self.cursor.position.line][:self.cursor.position.word]
        line = line.lower()
        reg = re.compile('[^а-я ]')
        line = reg.sub('', line)
        words = line.split()
        if len(words) == 0:
            return ''
        return words[-1]

    def get_prefix(self):
        line = self.content[self.cursor.position.line][:self.cursor.position.word]
        line = line.lower()
        reg = re.compile('[^а-я ]')
        line = reg.sub('', line)
        words = line.split()
        return words[-1:]
