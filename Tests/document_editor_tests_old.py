import unittest
from model.document_editor import DocumentEditor, Position
from model.document import Document


class CommonTests(unittest.TestCase):
    def test_mapping_is_correct1(self):
        document = Document('test.txt')
        document_editor = DocumentEditor(document, 6, 25)
        expected_content = ['abcd¶', 'abc·', 'abcde¶', 'ab']
        expected_old_to_new_line = [0, 1, 3]
        document_editor.update_content(Position(0, 0))
        self.assertEqual(expected_old_to_new_line, document_editor.old_to_new_line)
        self.assertEqual(expected_content, document_editor.content)

    def test_mapping_is_correct2(self):
        document = Document('test.txt')
        document_editor = DocumentEditor(document, 10, 25)
        expected_content = ['abcd¶', 'abc·abcde¶', 'ab']
        expected_old_to_new_line = [0, 1, 2]
        document_editor.update_content(Position(0, 0))
        self.assertEqual(expected_old_to_new_line, document_editor.old_to_new_line)
        self.assertEqual(expected_content, document_editor.content)


class CursorPositionTests(unittest.TestCase):
    def test_cursor_up(self):
        document = Document('test.txt')
        document_editor = DocumentEditor(document, 10, 25)
        document_editor.cursor


class TranslateAddressesTests(unittest.TestCase):
    def test_editor_to_original_position(self):
        document = Document('test.txt')
        document_editor = DocumentEditor(document, 6, 15)
        original_data = ['abcd\n', 'abc abcde\n', 'ab']
        document_editor.content = ['abcd\n', 'abc ', 'abcde\n', 'ab']
        document_editor.old_to_new_line = [0, 1, 3]
        for line in range(len(document_editor.content)):
            for i in range(len(document_editor.content[line])):
                symbol = document_editor.content[line][i]
                original_position = document_editor._editor_to_original_position(Position(line, i))
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

