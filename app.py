import curses
import pathlib

from model.global_session import Session


def draw(stdscr):
    session = Session(pathlib.Path('.'))
    session.loop(stdscr)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
