import time
import curses
import pathlib
import os

from FolderWindow import FolderWindow


class Program:
    from window import Window
    from EditorWindow import EditorWindow
    from FolderWindow import FolderWindow
    from NewFileWindow import NewFileWindow


def draw(stdscr):
    currentDirectory = pathlib.Path('.')
    window = FolderWindow(currentDirectory, Program())
    # window.draw()
    window.loop(stdscr)
    # folder_window(stdscr, currentDirectory)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
