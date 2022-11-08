import curses

from user_interface.drawer import draw_frame


class CreateFileWindow:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.content = ''

    def draw(self):
        self.stdscr.clear()
        width, height = draw_frame(self.stdscr, 'Creating file')
        self.stdscr.addstr(5, 1, '-' * width)
        self.stdscr.addstr(6, 1, self.content)
        self.stdscr.addstr(6, width - 5, '|.txt')
        self.stdscr.addstr(7, 1, '-' * width)
