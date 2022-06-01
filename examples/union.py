from algoaid import Graph

if __name__ == '__main__':
    # define graph
    edges = """
        4..0
        2..0
        1..2
        5..1
        9..5
        10..1
        12..0
        13..12
        14..12
        15..14
        6..14
        7..6
        8..6
        16..14
        22..12
        17..3
        18..17
        20..19
        11..20
        21..19
    """
    # construct
    g = Graph(edges, type=Graph.GraphType.DISJOINT_SET)
    # display
    g.display("Before Union")

    # Find with path compression (requires disjoint-set)
    g.show_find("6")

    # Union (requires disjoint-set)
    g.show_union("9", "11")
