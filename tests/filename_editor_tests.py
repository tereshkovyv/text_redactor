import unittest


from model.filename_editor import FilenameEditor

class FilenameEditorTests(unittest.TestCase):
    def test_t(self):
        filename_editor = FilenameEditor(True)
        filename_editor.add_char('a')
        filename_editor.add_char('b')
        filename_editor.add_char('\n')
        self.assertEqual(filename_editor.content, ['ab'])
        filename_editor.remove_char_backspace()
        self.assertEqual(filename_editor.content, ['a'])
        filename_editor.cursor.x = 0
        filename_editor.remove_char_delete()
        self.assertEqual(filename_editor.content, [''])
        filename_editor.remove_char_delete()
        filename_editor.remove_char_backspace()
        self.assertEqual(filename_editor.content [''])