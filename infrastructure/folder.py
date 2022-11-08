class Folder:
    def __init__(self, path):
        self.path = path
        self.content = ['...']
        for currentFile in path.iterdir():
            self.content.append(str(currentFile))