class Edge:
    def __init__(self, start, to, weight=None, marked=False):
        self.start = start
        self.to = to
        self.weight = weight
        self.marked = marked

    def reset(self):
        self.marked = False
