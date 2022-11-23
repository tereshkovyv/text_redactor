import curses

from ui.create_file_window import CreateFileWindow
from model.filename_editor import FilenameEditor
from controller.editor_session import EditorSession


class CreateFileSession:
    def __init__(self, stdscr, path, folder):
        self.folder = folder
        self.editor = FilenameEditor()
        self.stdscr = stdscr
        self.path = path
        self.window = CreateFileWindow(stdscr, self.editor)

    def loop(self):
        while True:
            self.window.draw()
            c = self.stdscr.getch()
            self.window.with_alert = False
            if c == 27:
                return
            if c == 10:
                if self.save():
                    return
            elif c == curses.KEY_LEFT:
                self.editor.cursor.left()
            elif c == curses.KEY_RIGHT:
                self.editor.cursor.right()
            elif c == 8:
                self.editor.remove_char_backspace()
            elif c == curses.KEY_DC:
                self.editor.remove_char_delete()
            else:
                c = chr(c)
                self.editor.add_char(c)

    def save(self):
        path = self.editor.content[0] + '.txt'
        if path in self.folder.content:
            self.window.with_alert = True
            return False
        else:
            with open(path, 'w+'):
                pass
            EditorSession(self.stdscr, path).loop()
            return True
