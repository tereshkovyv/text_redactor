import curses


def alert(stdscr, messege):
    isYes = False

    while True:
        c = stdscr.getch()
        if c == 260:
            isYes = True
        if c == 261:
            isYes = False
        if c == 115:
            return isYes
        draw(stdscr, isYes, messege)


def draw(stdscr, isyes, messege):
    stdscr.clear()
    stdscr.addstr(0, 0, messege)
    if isyes:
        stdscr.addstr(1, 0, 'YES', curses.A_REVERSE)
        stdscr.addstr(1, 5, 'NO')
    else:
        stdscr.addstr(1, 0, 'YES')
        stdscr.addstr(1, 5, 'NO', curses.A_REVERSE)
        stdscr.refresh()
