from .edge import Edge


class Node:
    def __init__(self, key):
        self.key = key
        self.adj = []
        self.visited = False
        self.parent = self
        self.size = 1
        self.dist = float('inf')
        self.indegree = 0

    def connect(self, other, weight=None):
        self.adj.append(Edge(self, other, weight))
        other.indegree += 1

    def reset(self):
        self.visited = False
        self.dist = float('inf')
        self.parent = self
        self.size = 1

    def sort_adj(self):
        self.adj = sorted(self.adj, key=lambda e: int(e.to.key))
