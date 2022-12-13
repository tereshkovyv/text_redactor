import unittest
import pathlib


from model.folder import Folder

class FolderTests(unittest.TestCase):
    def test_folder(self):
        folder = Folder(pathlib.Path('.'))
        self.assertTrue('folder_tests.py' in folder.content)