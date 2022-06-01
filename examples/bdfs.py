from algoaid import Graph

if __name__ == '__main__':
    # define graph
    edges = """
        0..4
        0..2
        0..5
        1..0
        2..1
        2..3
        3..6
        4..8
        5..6
        5..9
        5..10
        5..8
        6
        7..6
        8
        9..8
        9..10
        10..11
        11..7
    """
    # construct
    g = Graph(edges, type=Graph.GraphType.DI_GRAPH)

    # DFS
    g.dfs_tree("0")

    # BFS
    g.bfs_tree("0")
