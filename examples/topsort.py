from algoaid import Graph

if __name__ == '__main__':
    # define graph
    edges = """
        0..2 6
        0..1 1
        0..5 2
        0..4 1
        1..2 8
        4..8 7
        8..5 3
        8..9 4
        5..9 5
        9..10 2
        5..10 8
        5..6 20
        10..11 5
        6..11 8
        6..7 4
        6..3 1
        3..7 1
        7..11 3
        2..3 14
        2..5 3
    """
    # construct
    g = Graph(edges, type=Graph.GraphType.DI_GRAPH)

    # Topological sort
    g.topological_sort()
