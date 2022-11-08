import curses

from user_interface.drawer import draw_frame


class AlertWindow:
    def __init__(self, stdscr, messege):
        self.stdscr = stdscr
        self.messege = messege
        self.is_yes = False

    def draw(self):
        self.stdscr.clear()
        width, height = draw_frame(self.stdscr, self.messege)
        if self.is_yes:
            self.stdscr.addstr(5, width // 2 - 6, 'YES', curses.A_REVERSE)
            self.stdscr.addstr(5, width // 2 - 2, 'NO')
        else:
            self.stdscr.addstr(5, width // 2 - 6, 'YES')
            self.stdscr.addstr(5, width // 2 - 2, 'NO', curses.A_REVERSE)



