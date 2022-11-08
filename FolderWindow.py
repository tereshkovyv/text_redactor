from mailbox import linesep
import os
import time
import curses
import pathlib
import os
from Drawer import draw_frame
from window import Window

from AlertWindow import alert


class FolderWindow(Window):
    def __init__(self, directory, program):
        self.selected = 13
        self.program = program
        self.opened_folder = OpenedFolder(directory)

    def draw(self, stdscr, selected):
        stdscr.clear()

        draw_frame(stdscr, 'SUPER 100% TURBO TEXT REDACTOR PRO', '1 - create .txt file | 2 - delete file')

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

    def loop(self, stdscr):
        while True:
            elements = self.opened_folder.content
            self.draw(stdscr, self.selected)

            c = stdscr.getch()
            if c == 27:
                break
            if c == 259:
                self.selected = max(0, self.selected - 1)
            if c == 258:
                self.selected = min(self.selected + 1, len(elements) - 1)
            if c == 10:
                editor = self.program.EditorWindow(stdscr, elements[self.selected])
                editor.loop()

            # if c == 49:
            #    pass #create
            if c == 50:
                if alert(stdscr, "Are you sure?"):
                    os.remove(elements[self.selected])  # delete
            stdscr.addstr(0, 30, str(c))
            stdscr.refresh()


def get_elements(currentDirectory):
    elements = ['...']
    for currentFile in currentDirectory.iterdir():
        elements.append(str(currentFile))
    return elements


class OpenedFolder:
    def __init__(self, path):
        self.path = path

        self.content = ['...']
        for currentFile in path.iterdir():
            self.content.append(str(currentFile))

