import os


def draw_frame(stdscr, title):
    main_title = 'SUPER 100% TURBO TEXT REDACTOR PRO'
    columns = os.get_terminal_size().columns
    lines = os.get_terminal_size().lines

    stdscr.addstr(0, 0, '=' * columns)
    stdscr.addstr(1, (columns - len(main_title)) // 2, main_title)
    stdscr.addstr(2, 0, '-' * columns)
    stdscr.addstr(3, 2, title)
    stdscr.addstr(4, 0, '-' * columns)

    for i in range(1, lines - 1):
        try:
            stdscr.addstr(i, columns - 1, '|')
            stdscr.addstr(i, 0, '|')
        except:
            pass

    try:
        stdscr.addstr(lines - 1, 0, '=' * columns)
    except:
        pass
    return columns - 2, lines - 6
