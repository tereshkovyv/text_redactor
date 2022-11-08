import os

from supportive.alert_window import alert
from user_interface.folder_window import FolderWindow
from infrastructure.folder import Folder
from model.editor_session import EditorSession


class Session:
    def __init__(self, path):
        self.opened_folder = Folder(path)

        self.folder_window = FolderWindow(path, self.opened_folder)
        self.folder_window.selected = 7

    def loop(self, stdscr):
        while True:
            elements = self.opened_folder.content
            self.folder_window.draw(stdscr, self.folder_window.selected)

            c = stdscr.getch()
            if c == 27:
                break
            if c == 259:
                self.folder_window.selected = max(0, self.folder_window.selected - 1)
            if c == 258:
                self.folder_window.selected = min(self.folder_window.selected + 1, len(elements) - 1)
            if c == 10:
                editor = EditorSession(stdscr, elements[self.folder_window.selected])
                editor.loop()
            if c == 49:
                pass  # create
            if c == 50:
                if alert(stdscr, "Are you sure?"):
                    os.remove(elements[self.folder_window.selected])  # delete

            stdscr.addstr(0, 30, str(c))  # Вспомогательная хрень, которую нужно убрать
            stdscr.refresh()
