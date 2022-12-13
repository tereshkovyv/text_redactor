import os
import curses
from model.document_editor import DocumentEditor
from ui.editor_window import EditorWindow
from controller.alert_session import AlertSession
from model.document import Document
from infrastructure.cursor_hit_the_edge_exception import CursorHitTheEdgeException


class EditorSession:
    def __init__(self, stdscr, path):
        self.stdscr = stdscr

        self.document = Document(path)
        self.editor = DocumentEditor(self.document, os.get_terminal_size().columns - 2, os.get_terminal_size().lines - 6)
        self.window = EditorWindow(path, self.editor)

    def __enter__(self):
        self.document.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.document.__exit__(None, None, None)

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
                try:
                    self.editor.cursor.up()
                except CursorHitTheEdgeException:
                    self.editor.line_up()
            elif c == curses.KEY_DOWN:
                try:
                    self.editor.cursor.down()
                except CursorHitTheEdgeException:
                    self.editor.line_down()
            elif c == curses.KEY_LEFT:
                self.editor.cursor.left()
            elif c == curses.KEY_RIGHT:
                self.editor.cursor.right()
            elif c == 8:
                self.editor.remove_char_backspace()
            elif c == 9:
                self.editor.autocomplete_word()
            elif c == curses.KEY_DC:
                self.editor.remove_char_delete()
            else:
                c = chr(c)
                self.editor.add_char(c)
