# algoaid
A collection of useful tools for students taking an introductory course in algorithms and data structures.

# Installation
```bash
pip install algoaid
```

# Features
- Time complexity analysis of functions
- Graphs
    - Represent: [weighted] [un]directed, disjoint-set/union find
    - Easy to input a graph
    - Run basic graph algorithms (DFS, BFS, MST, Dijkstra's and more)
    - Visualise results 
- Versatile Min/Max-heap with `decrease/increase` key functionality


# Modules
- Time complexity: `analyse`
- Graph class: `Graph`
- Priority queues: `MinHeap`, `MaxHeap`


# Usage: Time Complexity Analysis
Analyse time complexity of a function with a single parameter:
#### 1. Import
```python
from algoaid import analyse
```
#### 2. Define a Function
```python
def f(n):
    j = 1
    while j * j < n:
        j += 1
```
#### 3. Analyse
```python
analyse(f)
```

### Example Result
<p align="left">
  <img src="https://i.imgur.com/p3lbLgD.png" width="500">
</p>


# Usage: Graphs
Construct various types of graphs and run a selection of popular graph algorithms:
#### 1. Import
```python
from algoaid import Graph
```
#### 2. Declare the Graph (each line represents an edge)
```python
edges = """
    0..2 6
    0..1 1
    0..5 2
    .
    .
    .
    2..5 4
"""
```
Syntax:
- Undirected: `[node1]..[node2] [weight (optional)]`
- Directed: `[from]..[to] [weight (optional)]`
- Disjoint-set: `[parent]..[child]`

#### 3. Construct the Graph
```python
# construct undirected graph
g = Graph(edges, type=Graph.GraphType.GRAPH)

# construct directed graph
g = Graph(edges, type=Graph.GraphType.DI_GRAPH)

# construct disjoint set
g = Graph(edges, type=Graph.GraphType.DISJOINT_SET)
```

#### 4. Display the Graph
```python
g.display("My Graph")
```

#### 5. Run Algorithms
```python
# Run DFS from node 0
g.dfs_tree("0")

# Run BFS from node 0
g.bfs_tree("0")

# Compute MST (requires a weighted undirected graph)
g.mst_tree()

# Run Dijkstra's algorithm from node 0 (requires a weighted graph)
g.dijkstra_tree("0")

# Topological sorting (requires a directed graph)
g.topological_sort()

# Find with path compression (requires disjoint-set)
g.show_find("6")

# Union (requires disjoint-set)
g.show_union("9", "11")

```

### Example Results
<p align="left">
  <img src="https://i.imgur.com/5OWU2yK.png" width="700">
</p>
<p align="left">
  <img src="https://i.imgur.com/eth54X4.png" width="500">
</p>
<p align="left">
  <img src="https://i.imgur.com/yKTQ8Bn.png" width="500">
</p>







