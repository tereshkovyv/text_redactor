import time
import curses
import pathlib
import os



def draw(stdscr):

    currentDirectory = pathlib.Path('..')
    folder_window(stdscr, currentDirectory)

def folder_window(stdscr, currentDirectory):
    
    selected = 6

    while True:
        elements = get_elements(currentDirectory)
        draw_files_list(stdscr, get_elements(currentDirectory), selected)

        c = stdscr.getch()
        if c == 27:
            break
        if c == 259:
            selected = max(0, selected-1)
        if c == 258:
            selected= min(selected + 1, len(elements)-1)
        if c == 115:
            file_window(stdscr, elements[selected])
        if c == 49:
            pass #create
        if c == 50:
            if sure_window(stdscr):
                os.remove(elements[selected])# delete
        stdscr.addstr(0, 30, str(c))
        stdscr.refresh()
            
            

def sure_window(stdscr):
    isyes = False
    draw_sure_window(stdscr, isyes)
    while True:
        c = stdscr.getch()
        if c == 260:
            isyes = True
        if c == 261:
            isyes = False
        if c == 115:
            return isyes
        draw_sure_window(stdscr, isyes)


def draw_sure_window(stdscr, isyes):
    stdscr.clear()
    stdscr.addstr(0, 0, 'Are you sure?')
    if isyes:
        stdscr.addstr(1, 0, 'YES', curses.A_REVERSE)
        stdscr.addstr(1, 5, 'NO')
    else:
        stdscr.addstr(1, 0, 'YES')
        stdscr.addstr(1, 5, 'NO', curses.A_REVERSE)
        stdscr.refresh()


def file_window(stdscr, path):

    while True:
        draw_document(stdscr, path)

        c = stdscr.getch()
        if c == 27:
            break


    #time.sleep(3)

def draw_files_list(stdscr, elements, selected):
    stdscr.clear()
    stdscr.addstr(0, 0, 'WELCOME TO MY TEXT REDACTOR!')
    stdscr.addstr(1, 0, '---------------------------')
    stdscr.addstr(2, 0, '1 - create .txt file | 2 - delete file')
    stdscr.addstr(3, 0, '---------------------------')
    
    for i in range(len(elements)):
        if i == selected:
            stdscr.addstr(i+4, 0, '||' +  str(elements[i]), curses.A_REVERSE)
        else:
            stdscr.addstr(i+4, 0, '||' + str(elements[i]))
        stdscr.refresh()

def draw_document(stdscr, path):
    stdscr.clear()
    stdscr.addstr(0, 0, str(path))
    stdscr.addstr(1, 0, '-----------')
 
    i = 2
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            stdscr.addstr(i, 0, str(i-2) + '|' + line)
            i += 1

    stdscr.refresh()

def get_elements(currentDirectory):
    elements = ['...']
    for currentFile in currentDirectory.iterdir():
        elements.append(str(currentFile))
    return elements

if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
