import unittest
from model.document_editor import DocumentEditor, Position
from model.document import Document


class DocumentEditorTests(unittest.TestCase):
    def test_test1(self):
        with Document('test2.txt') as document:
            document_editor = DocumentEditor(document, 9, 3, True)

            expected_content1 = ['-Привет, ', '1ак дела?', '-Хорош0, ']
            expected_new_to_old_line1 = ['(0, 0)', '(0, 9)', '(1, 0)']
            document_editor.update_content()
            content = document_editor.content
            new_to_old_line = [str(x) for x in document_editor.new_to_old_line]

            self.assertListEqual(expected_new_to_old_line1, new_to_old_line)
            self.assertEqual(expected_content1, content)

            document_editor.line_down()
            document_editor.line_down()
            document_editor.line_down()
            document_editor.line_up()

            expected_content2 = ['-Хорош0, ', '1 у тебя?', '-Тоже ']
            expected_new_to_old_line2 = ['(0, 0)', '(0, 9)', '(1, 0)', '(1, 9)', '(2, 0)']
            content = document_editor.content
            new_to_old_line = [str(x) for x in document_editor.new_to_old_line]

            self.assertEqual(expected_content2, content)
            self.assertListEqual(expected_new_to_old_line2, new_to_old_line)

            document_editor.line_down()
            document_editor.line_down()

            expected_content3 = ['-Тоже ', 'ничего.']
            content = document_editor.content
            self.assertEqual(expected_content3, content)


    def test_editor_to_original_position(self):
        with Document('test2.txt') as document:
            document_editor = DocumentEditor(document, 9, 3, True)
            document_editor._get_content()
            document_editor._starting_line = 2
            document_editor._get_content()
            document_editor._starting_line = 3
            document_editor._get_content()
            self.assertEqual(str(document_editor._editor_to_original_position(Position(0, 6))), str(Position(1, 15)))

    def test_edit_chars(self):
        with Document('test2.txt') as document:
            document_editor = DocumentEditor(document, 9, 3, True)
            document_editor.update_content()
            document_editor.cursor.x = 1
            document_editor.remove_char_backspace()
            expected_content = ['Привет, 1', 'ак дела?', '-Хорош0, ']
            self.assertEqual(document_editor.content, expected_content)
            document_editor.add_char('-')
            expected_content = ['-Привет, ', '1ак дела?', '-Хорош0, ']
            self.assertEqual(document_editor.content, expected_content)
            document_editor.remove_char_delete()
            expected_content = ['-ривет, 1', 'ак дела?', '-Хорош0, ']
            self.assertEqual(document_editor.content, expected_content)
            document_editor.add_char('\n')
            expected_content = ['-', 'ривет, 1', 'ак дела?']
            self.assertEqual(document_editor.content, expected_content)