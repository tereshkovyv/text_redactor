import curses
import pathlib

from controller.folder_session import FolderSession


def draw(stdscr):
    FolderSession(pathlib.Path('.')).loop(stdscr)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
