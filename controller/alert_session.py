from ui.alert_window import AlertWindow


class AlertSession:
    def __init__(self, stdscr, message):
        self.stdscr = stdscr
        self.window = AlertWindow(stdscr, message)

    def loop(self):
        while True:
            self.window.draw()
            c = self.stdscr.getch()
            if c == 27:
                return False
            if c == 260:
                self.window.is_yes = True
            if c == 261:
                self.window.is_yes = False
            if c == 10:
                return self.window.is_yes
