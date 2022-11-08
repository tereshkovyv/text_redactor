import unittest
from infrastructure.document_editor import DocumentEditor, Position


class WorkTimeTests(unittest.TestCase):
    def test_editor_to_original_position(self):
        doc = DocumentEditor("C:\\Users\\Yuri\\Desktop\\Python\\TextRedactor\\text_redactor\\Tests\\test.txt", 6, 15)
        original_data = ['abcd\n', 'abc abcde\n', 'ab']
        doc.content = ['abcd\n', 'abc ', 'abcde\n', 'ab']
        doc.old_to_new_line = [0, 1, 3]
        for line in range(len(doc.content)):
            for i in range(len(doc.content[line])):
                symbol = doc.content[line][i]
                original_position = doc.editor_to_original_position(Position(line, i))
                original_symbol = original_data[original_position.line][original_position.word]
                self.assertEqual(symbol, original_symbol, symbol + " not equal to " + original_symbol)

    def test_original_to_editor_position(self):
        doc = DocumentEditor("C:\\Users\\Yuri\\Desktop\\Python\\TextRedactor\\text_redactor\\Tests\\test.txt", 6, 15)
        original_data = ['abcd\n', 'abc abcde\n', 'ab']
        doc.content = ['abcd\n', 'abc ', 'abcde\n', 'ab']
        doc.old_to_new_line = [0, 1, 3]
        for line in range(len(original_data)):
            for i in range(len(original_data[line])):
                symbol = original_data[line][i]
                original_position = doc.original_to_editor_position(Position(line, i))
                editor_symbol = doc.content[original_position.line][original_position.word]
                self.assertEqual(symbol, editor_symbol, symbol + " not equal to " + editor_symbol)