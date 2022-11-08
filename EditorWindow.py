import os
import curses
from infrastructure.document_editor import DocumentEditor
from infrastructure.document import Document
from infrastructure.position import Position
from Drawer import draw_frame
from window import Window


class EditorWindow(Window):
    def __init__(self, stdscr, path):
        self.stdscr = stdscr
        self.path = path
        self.first_line_index = 0
        self.word_index = 0

        self.document = DocumentEditor(path, os.get_terminal_size().columns - 2, os.get_terminal_size().lines - 6)

    def loop(self):
        while True:
            self.draw(self.stdscr)

            c = self.stdscr.getch()
            if c == 27:
                break
            if c == curses.KEY_UP:
                self.document.add_char()
                #self.document.cursor.up()
            if c == curses.KEY_DOWN:
                self.document.cursor.down()
            if c == curses.KEY_LEFT:
                self.document.cursor.left()
            if c == 8:
                self.document.remove_char_backspace()
            if c == curses.KEY_DC:
                self.document.remove_char_delete()
            if c == curses.KEY_RIGHT:
                self.document.cursor.right()
            self.stdscr.move(self.document.cursor.y + 5, self.document.cursor.x + 1)

    def draw(self, stdscr):
        stdscr.clear()
        (self.width, self.height) = draw_frame(stdscr, 'SUPER 100% TURBO TEXT REDACTOR PRO', str(self.path))
        i = 5
        self.document.update_content(Position(0, 0))
        for line in self.document.content:
            try:
                stdscr.addstr(i, 1, line)
            except:
                pass
            i += 1

        # stdscr.addstr(self.document.cursor.y + 5, self.document.cursor.x + 1, self.document.current_char,
        #               curses.A_REVERSE)
        stdscr.refresh()
        stdscr.move(self.document.cursor.y + 5, self.document.cursor.x + 1)



