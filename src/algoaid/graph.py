import graphviz
from queue import Queue
from .priority import MinHeap
from enum import Enum
from .node import Node


class Graph:
    class GraphType(Enum):
        GRAPH = "an undirected graph"
        DI_GRAPH = "a directed graph"
        DISJOINT_SET = "a disjoint Set"

    def __init__(self, string, type: GraphType):
        self.nodes = dict()
        self.type = type

        for line in string.split('\n'):
            line = line.strip()
            if ".." not in line:
                if len(line) > 0:
                    if line not in self.nodes:
                        self.nodes[line] = Node(line)
                continue

            args = line.replace("..", " ").split(" ")
            if len(args) == 3:
                (a, b, w) = args
                w = int(w)
            else:
                (a, b) = args
                w = None
            # add nodes if new
            if a not in self.nodes:
                self.nodes[a] = Node(a)
            if b not in self.nodes:
                self.nodes[b] = Node(b)
            # connect
            if self.type == self.GraphType.DISJOINT_SET:
                self.nodes[a].parent = self.nodes[b]
            else:
                self.nodes[a].connect(self.nodes[b], w)
                if self.type == self.GraphType.GRAPH:
                    self.nodes[b].connect(self.nodes[a], w)

        # sort ascending
        for node in self.nodes.values():
            node.sort_adj()

    def get_edges(self):
        edges = []
        seen = set()
        for node in self.nodes.values():
            for edge in node.adj:
                if self.type == self.GraphType.DI_GRAPH:
                    h = (edge.start, edge.to)
                else:
                    h = hash(frozenset({edge.start, edge.to}))
                if h not in seen:
                    seen.add(h)
                    edges.append(edge)
        return edges

    def display(self, title="Graph"):
        atts = {'nodesep': '.3', 'ranksep': '.3'}
        dot = graphviz.Graph(title, graph_attr=atts)
        if self.type == self.GraphType.DI_GRAPH:
            dot = graphviz.Digraph(title, graph_attr=atts)
        # print nodes
        for node in self.nodes.values():
            if node.dist < float('inf'):
                dot.node(node.key, f"<<B>{node.key}</B> ({node.dist})>")
            else:
                dot.node(node.key, f"<<B>{node.key}</B>>")
        # print edges
        if self.type == self.GraphType.DISJOINT_SET:
            for node in self.nodes.values():
                if node.parent != node:
                    fillcolor = 'red' if node.visited else None
                    dot.edge(node.parent.key, node.key, color=fillcolor)
        else:
            for edge in self.get_edges():
                label = " " + str(edge.weight) + \
                    " " if edge.weight is not None else None
                fillcolor = 'red' if edge.marked else None
                dot.edge(edge.start.key, edge.to.key,
                         label=label, color=fillcolor)
        dot.render(directory='renders', view=True)

    def reset(self):
        for node in self.nodes.values():
            node.reset()
            for edge in node.adj:
                edge.reset()

    def get_node(self, name):
        return self.nodes[name]

    def dfs(self, node):
        node.visited = True
        for edge in node.adj:
            if not edge.to.visited:
                edge.marked = True
                if self.type == Graph.GraphType.GRAPH:
                    next(e for e in edge.to.adj if e.to == node).marked = True
                self.dfs(edge.to)

    def dfs_tree(self, start):
        self.reset()
        start = self.get_node(start)

        self.dfs(start)
        self.display("DFS tree")

    def bfs_tree(self, start):
        self.reset()
        start = self.get_node(start)
        q = Queue()
        q.put(start)
        start.visited = True
        start.dist = 0
        while not q.empty():
            node = q.get()
            for edge in node.adj:
                if not edge.to.visited:
                    edge.marked = True
                    edge.to.dist = node.dist + 1
                    q.put(edge.to)
                    edge.to.visited = True
        self.display("BFS tree")

    def mst_tree(self):
        if self.type not in [self.GraphType.GRAPH, self.GraphType.DI_GRAPH]:
            raise Exception(f"MST can not be run on {self.type}")

        self.reset()
        edges = sorted(self.get_edges(), key=lambda e: e.weight)
        included = []
        total = 0

        for edge in edges:
            if self.union(edge.start, edge.to):
                edge.marked = True
                included.append(edge)
                total += edge.weight

        self.display("MST")
        print(f"MST: total weight is {total}")

    def dijkstra_tree(self, start):
        if self.type not in [self.GraphType.GRAPH, self.GraphType.DI_GRAPH]:
            raise Exception(f"Dijkstra can not be run on {self.type}")

        start = self.get_node(start)
        self.reset()
        q = MinHeap()

        for node in self.nodes.values():
            q.insert(node, node.dist)

        start.dist = 0
        q.decrease_key(start, 0)

        while not q.empty():
            node = q.extract_min()
            for edge in node.adj:
                # relax
                if edge.to.dist > node.dist + edge.weight:
                    edge.to.dist = node.dist + edge.weight
                    edge.to.parent = node
                    q.decrease_key(edge.to, edge.to.dist)

        # mark edges
        for edge in self.get_edges():
            if edge.to.parent == edge.start:
                edge.marked = True

        self.display("DIJKSTRA")

    def topological_sort(self):
        if self.type != self.GraphType.DI_GRAPH:
            raise Exception(
                f"Topological sort can not be run on {self.type.value}")

        self.reset()
        sorting = []
        ready = []
        nodes = self.nodes.values()
        for node in nodes:
            node.size = node.indegree
            if node.size == 0:
                ready.append(node)
                node.visited = True

        while len(ready) > 0:
            current = ready.pop()
            sorting.append(current)
            for edge in current.adj:
                other = edge.to
                if other.size > 0:
                    other.size -= 1
                    if other.size == 0:
                        other.visited = True
                        ready.append(other)

        print("TOPOLOGICAL SORT:")
        if len(sorting) < len(nodes):
            print("Failed!")
        else:
            for (i, node) in enumerate(sorting):
                node.dist = i
                print(node.key, end=" ")
            print()
            self.display("TOPOLOGICAL SORT")

    def find(self, x):
        if x.parent != x:
            old_parent = x.parent
            x.parent = self.find(x.parent)
            if x.parent != old_parent:
                x.visited = True
        return x.parent

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if x.size >= y.size:
                y.parent = x
                x.size += y.size
            else:
                x.parent = y
                y.size += x.size
            return True
        return False

    def show_find(self, x):
        self.find(self.get_node(x))
        self.display(f"Disjoint-set after find({x})")

    def show_union(self, x, y):
        self.union(self.get_node(x), self.get_node(y))
        self.display(f"Disjoint-set after union({x}, {y})")
