import unittest
from model.document_editor import DocumentEditor, Position
from model.document import Document


class CommonTests(unittest.TestCase):
    def test_test1(self):
        document = Document('test2.txt')
        document_editor = DocumentEditor(document, 9, 3)

        expected_content1 = ['-Привет, ', 'как дела?', '-Хорошо, ']
        expected_new_to_old_line1 = ['(0, 0)', '(0, 9)', '(1, 0)']
        content, new_to_old_line = document_editor._get_content()
        new_to_old_line = [str(x) for x in new_to_old_line]

        self.assertListEqual(expected_new_to_old_line1, new_to_old_line)
        self.assertEqual(expected_content1, content)

        document_editor.starting_line = 2
        document_editor._get_content()

        expected_content2 = ['а у тебя?', '-Тоже ', 'ничего.']
        expected_new_to_old_line2 = ['(0, 0)', '(0, 9)', '(1, 0)', '(1, 9)', '(2, 0)', '(2, 6)']
        document_editor.starting_line = 2
        content, new_to_old_line = document_editor._get_content()
        new_to_old_line = [str(x) for x in new_to_old_line]

        self.assertEqual(expected_content2, content)
        self.assertListEqual(expected_new_to_old_line2, new_to_old_line)

    def test_editor_to_original_position(self):
        document = Document('test2.txt')
        document_editor = DocumentEditor(document, 9, 3)
        document_editor._get_content()
        document_editor.starting_line = 2
        document_editor._get_content()
        document_editor.starting_line = 3
        document_editor._get_content()
        self.assertEqual(str(document_editor._editor_to_original_position(Position(0, 6))), str(Position(1, 15)))