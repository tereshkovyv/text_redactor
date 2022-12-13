import unittest
from model.document import Document
from infrastructure.position import Position


class DocumentTests(unittest.TestCase):
    def test_no_action(self):
        with Document('test.txt') as document:
            expected_content = ['abcd\n', 'abc abcde\n', 'ab']
            for _ in document:
                pass
            self.assertEqual(expected_content, document.data)
            self.assertEqual(expected_content, [x for x in document.data_in_lines(0)])

    def test_add_char(self):
        with Document('test.txt') as document:
            for _ in document:
                pass
            position_to_insert = Position(0, 2)
            document.add_common_char(position_to_insert, 'x')
            expected_content = ['abxcd\n', 'abc abcde\n', 'ab']
            self.assertEqual(expected_content, document.data)

    def test_add_new_line_char(self):
        with Document('test.txt') as document:
            for _ in document:
                pass
            position_to_insert = Position(0, 2)
            document.add_new_line_char(position_to_insert)
            expected_content = ['ab\n', 'cd\n', 'abc abcde\n', 'ab']
            self.assertEqual(expected_content, document.data)

    def test_add_new_line_char2(self):
        with Document('test.txt') as document:
            for _ in document:
                pass
            position_to_insert = Position(0, 4)
            document.add_new_line_char(position_to_insert)
            expected_content = ['abcd\n', '\n', 'abc abcde\n', 'ab']
            self.assertEqual(expected_content, document.data)

    def test_backspace_char(self):
        with Document('test.txt') as document:
            for _ in document:
                pass
            position = Position(0, 2)
            document.backspace_char(position)
            expected_content = ['acd\n', 'abc abcde\n', 'ab']
            self.assertEqual(expected_content, document.data)

    def test_delete_char(self):
        with Document('test.txt') as document:
            for _ in document:
                pass
            position = Position(0, 2)
            document.delete_char(position)
            expected_content = ['abd\n', 'abc abcde\n', 'ab']
            self.assertEqual(expected_content, document.data)

    def test_backspace_new_line_char(self):
        with Document('test.txt') as document:
            for _ in document:
                pass
            position = Position(1, 0)
            document.backspace_char(position)
            expected_content = ['abcdabc abcde\n', 'ab']
            self.assertEqual(expected_content, document.data)

    def test_backspace_single_char(self):
        with Document('test.txt') as document:
            for _ in document:
                pass
            position = Position(2, 2)
            document.backspace_char(position)
            position = Position(2, 1)
            document.backspace_char(position)
            expected_content = ['abcd\n', 'abc abcde\n']
        self.assertEqual(expected_content, document.data)

    def test_delete_new_line_char(self):
        with Document('test.txt') as document:
            for _ in document:
                pass
            position = Position(0, 4)
            document.delete_char(position)
            expected_content = ['abcdabc abcde\n', 'ab']
            self.assertEqual(expected_content, document.data)

    def test_delete_single_char(self):
        with Document('test.txt') as document:
            for _ in document:
                pass
            position = Position(2, 2)
            document.backspace_char(position)
            position = Position(2, 0)
            document.delete_char(position)
            expected_content = ['abcd\n', 'abc abcde\n']
            self.assertEqual(expected_content, document.data)
    def test_delete_char_at_last_position(self):
        with Document('test.txt') as document:
            for _ in document:
                pass
            position = Position(2, 1)
            document.delete_char(position)
            expected_content = ['abcd\n', 'abc abcde\n', 'ab']
            self.assertEqual(expected_content, document.data)

    def test_backspace_char_at_first_position(self):
        with Document('test.txt') as document:
            for _ in document:
                pass
            position = Position(0, 0)
            document.backspace_char(position)
            expected_content = ['abcd\n', 'abc abcde\n', 'ab']
            self.assertEqual(expected_content, document.data)