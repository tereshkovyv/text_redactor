import os

from controller.alert_session import AlertSession
from ui.folder_window import FolderWindow
from model.folder import Folder
from controller.editor_session import EditorSession
from controller.create_file_session import CreateFileSession


class FolderSession:
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
                with EditorSession(stdscr, elements[self.folder_window.selected]) as session:
                    session.loop()
            if c == 49:
                CreateFileSession(stdscr, self.opened_folder.path, self.opened_folder).loop()
                self.opened_folder.refresh()
            if c == 50:
                if AlertSession(stdscr, "Delete '" + str(elements[self.folder_window.selected]) + "' ?").loop():
                    os.remove(elements[self.folder_window.selected])
                self.opened_folder.refresh()

            stdscr.refresh()
