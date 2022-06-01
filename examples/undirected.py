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
    """
    # construct graph
    g = Graph(edges, type=Graph.GraphType.GRAPH)

    # DFS
    g.dfs_tree("0")

    # BFS
    g.bfs_tree("0")

    # Compute MST, requires a weighted graph!
    g.mst_tree()
