class Folder:
    def __init__(self, path):
        self.path = path
        self.content = ['...']
        self.refresh()

    def refresh(self):
        self.content = []
        for currentFile in self.path.iterdir():
            self.content.append(str(currentFile))
