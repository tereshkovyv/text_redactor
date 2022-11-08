


class Editor:
    def __init__(self, path):
        self.path = path

    def get_lines(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f:
                yield line