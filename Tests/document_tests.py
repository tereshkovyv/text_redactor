import unittest
from infrastructure.document import Document
from infrastructure.position import Position


class DocumentTests(unittest.TestCase):
    def test_no_action(self):
        document = Document('test.txt')
        expected_content = ['abcd\n', 'abc abcde\n', 'ab']
        self.assertEqual(expected_content, document.data)

    def test_add_char(self):
        document = Document('test.txt')
        position_to_insert = Position(0, 2)
        document.add_char(position_to_insert, 'x')
        expected_content = ['abxcd\n', 'abc abcde\n', 'ab']
        self.assertEqual(expected_content, document.data)

    def test_add_new_line_char(self):
        document = Document('test.txt')
        position_to_insert = Position(0, 2)
        document.add_new_line_char(position_to_insert)
        expected_content = ['ab\n', 'cd\n', 'abc abcde\n', 'ab']
        self.assertEqual(expected_content, document.data)

    def test_add_new_line_char2(self):
        document = Document('test.txt')
        position_to_insert = Position(0, 4)
        document.add_new_line_char(position_to_insert)
        expected_content = ['abcd\n', '\n', 'abc abcde\n', 'ab']
        self.assertEqual(expected_content, document.data)

    def test_backspace_char(self):
        document = Document('test.txt')
        position = Position(0, 2)
        document.backspace_char(position)
        expected_content = ['acd\n', 'abc abcde\n', 'ab']
        self.assertEqual(expected_content, document.data)

    def test_delete_char(self):
        document = Document('test.txt')
        position = Position(0, 2)
        document.del_char(position)
        expected_content = ['abd\n', 'abc abcde\n', 'ab']
        self.assertEqual(expected_content, document.data)

    def test_backspace_new_line_char(self):
        document = Document('test.txt')
        position = Position(1, 0)
        document.backspace_char(position)
        expected_content = ['abcdabc abcde\n', 'ab']
        self.assertEqual(expected_content, document.data)

    def test_delete_new_line_char(self):
        document = Document('test.txt')
        position = Position(0, 4)
        document.del_char(position)
        expected_content = ['abcdabc abcde\n', 'ab']
        self.assertEqual(expected_content, document.data)

    def test_delete_char_at_last_position(self):
        document = Document('test.txt')
        position = Position(2, 1)
        document.del_char(position)
        expected_content = ['abcd\n', 'abc abcde\n', 'ab']
        self.assertEqual(expected_content, document.data)

    def test_backspace_char_at_first_position(self):
        document = Document('test.txt')
        position = Position(0, 0)
        document.backspace_char(position)
        expected_content = ['abcd\n', 'abc abcde\n', 'ab']
        self.assertEqual(expected_content, document.data)