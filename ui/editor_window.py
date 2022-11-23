from ui.drawer import draw_frame


class EditorWindow:
    def __init__(self, path, editor):
        self.path = path
        self.editor = editor

    def draw(self, stdscr):
        stdscr.clear()
        (self.width, self.height) = draw_frame(stdscr, str(self.path))
        i = 5
        self.editor.update_content()
        for line in self.editor.content:
            stdscr.addstr(i, 1, line)
            i += 1

        stdscr.refresh()
        try:
            stdscr.move(self.editor.cursor.y + 5, self.editor.cursor.x + 1)
        except:
            pass
