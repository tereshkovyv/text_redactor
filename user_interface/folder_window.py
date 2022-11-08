import curses
from user_interface.drawer import draw_frame


class FolderWindow():
    def __init__(self, directory, opened_folder):
        self.selected = 13
        self.opened_folder = opened_folder

    def draw(self, stdscr, selected):
        stdscr.clear()

        draw_frame(stdscr, '1 - create .txt file | 2 - delete file')

        for i in range(len(self.opened_folder.content)):
            if i == selected:
                try:
                    stdscr.addstr(i + 5, 2, '||' + str(self.opened_folder.content[i]), curses.A_REVERSE)
                except:
                    pass
            else:
                try:
                    stdscr.addstr(i + 5, 2, '||' + str(self.opened_folder.content[i]))
                except:
                    pass
            stdscr.refresh()

