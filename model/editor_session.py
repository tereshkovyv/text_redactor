import os
import curses
from model.document_editor import DocumentEditor
from user_interface.editor_window import EditorWindow


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
                break
            if c == curses.KEY_UP:
                self.editor.add_char()
                # self.document.cursor.up()
            if c == curses.KEY_DOWN:
                self.editor.cursor.down()
            if c == curses.KEY_LEFT:
                self.editor.cursor.left()
            if c == curses.KEY_RIGHT:
                self.editor.cursor.right()
            if c == 8:
                self.editor.remove_char_backspace()
            if c == curses.KEY_DC:
                self.editor.remove_char_delete()

            self.stdscr.move(self.editor.cursor.y + 5, self.editor.cursor.x + 1)