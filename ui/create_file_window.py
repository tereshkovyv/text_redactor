import curses

from ui.drawer import draw_frame


class CreateFileWindow:
    def __init__(self, stdscr, editor):
        self.stdscr = stdscr
        self.editor = editor
        self.with_alert = False

    def draw(self):
        self.stdscr.clear()
        width, height = draw_frame(self.stdscr, 'Creating file')
        self.stdscr.addstr(5, 1, '-' * width)
        self.stdscr.addstr(6, 1, self.editor.content[0])
        self.stdscr.addstr(6, width - 5, '|.txt')
        self.stdscr.addstr(7, 1, '-' * width)

        if self.with_alert:
            self.stdscr.addstr(8, 1, 'File already exist')

        self.stdscr.refresh()
        self.stdscr.move(self.editor.cursor.y + 6, self.editor.cursor.x + 1)