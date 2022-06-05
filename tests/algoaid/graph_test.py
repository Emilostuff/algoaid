from src.algoaid.graph import Graph

EDGES_WEIGHTS = """
    0..2 6
    0..1 1
    0..5 2
    0..4 1
    1..2 8
    4..8 7
    8..5 3
"""


def test_graph_nodes():
    # construct graph
    g = Graph(EDGES_WEIGHTS, type=Graph.GraphType.GRAPH)
    dg = Graph(EDGES_WEIGHTS, type=Graph.GraphType.DI_GRAPH)

    for node in ["0", "1", "2", "4", "5", "8"]:
        assert node in g.nodes
        assert node in dg.nodes


def test_get_edges_digraph():
    # construct graph
    g = Graph(EDGES_WEIGHTS, type=Graph.GraphType.DI_GRAPH)

    edges = [(0, 2, 6), (0, 1, 1), (0, 5, 2), (0, 4, 1),
             (1, 2, 8), (4, 8, 7), (8, 5, 3)]
    graph_edges = g.get_edges()
    assert len(edges) == len(graph_edges)

    for (a, b, w) in edges:
        # print(a, b, w)
        # print([f"{e.start.key}..{e.to.key} {e.weight}" for e in graph_edges])
        assert any(
            [e.start.key == str(a) and e.to.key == str(
                b) and e.weight == w for e in graph_edges]
        )
