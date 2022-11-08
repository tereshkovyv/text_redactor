from user_interface.alert_window import AlertWindow
from user_interface.create_file_window import CreateFileWindow


class CreateFileSession:
    def __init__(self, stdscr, path):
        self.stdscr = stdscr
        self.path = path
        self.window = CreateFileWindow(stdscr)

    def loop(self):
        while True:
            self.window.draw()
            c = self.stdscr.getch()
            if c == 27:
                return 'exit'

            if c == 10:
                return 'save'
