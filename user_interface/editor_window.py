from infrastructure.position import Position
from user_interface.drawer import draw_frame


class EditorWindow:
    def __init__(self, path, editor):
        self.path = path
        self.editor = editor

    def draw(self, stdscr):
        stdscr.clear()
        (self.width, self.height) = draw_frame(stdscr, str(self.path))
        i = 5
        self.editor.update_content(Position(0, 0))
        for line in self.editor.content:
            stdscr.addstr(i, 1, line)
            i += 1

        # stdscr.addstr(self.document.cursor.y + 5, self.document.cursor.x + 1, self.document.current_char,
        #               curses.A_REVERSE)
        stdscr.refresh()
        stdscr.move(self.editor.cursor.y + 5, self.editor.cursor.x + 1)
