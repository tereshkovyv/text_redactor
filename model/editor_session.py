import os
import curses
from model.document_editor import DocumentEditor
from user_interface.editor_window import EditorWindow
from model.alert_session import AlertSession


class EditorSession:
    def __init__(self, stdscr, path):
        self.stdscr = stdscr

        self.editor = DocumentEditor(path, os.get_terminal_size().columns - 2, os.get_terminal_size().lines - 6)
        self.window = EditorWindow(path, self.editor)

    def loop(self):
        while True:
            self.window.draw(self.stdscr)
            c = self.stdscr.getch()
            if c == 27:
                if not self.editor.modified:
                    break
                if AlertSession(self.stdscr, 'Save changes?').loop():
                    self.editor.document.save()

                break
            elif c == curses.KEY_UP:
                self.document.cursor.up()
            elif c == curses.KEY_DOWN:
                self.editor.cursor.down()
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

            self.stdscr.move(self.editor.cursor.y + 5, self.editor.cursor.x + 1)