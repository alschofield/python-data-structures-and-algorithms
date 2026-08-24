# Adjacency Matrix

## How It Works

A dynamically grown N by N weighted edge grid indexed by node-handle indexes; the dense graph representation.

## Required API

Implement `AdjacencyMatrix[T]` with: `create(directed)`, `add_node(value) -> NodeHandle`, `find_node(value) -> NodeHandle | None`, `node_at(index) -> NodeHandle | None`, `node_value(node) -> T | None`, `add_edge(from_node, to_node, weight)`, `remove_edge`, `has_edge`, `neighbors(node)`, `node_count`, `edge_count`, and `as_graph_view() -> GraphView[T]`. `neighbors(node)` yields deterministic `(NodeHandle, weight)` edges.

## Contract

- `create` starts empty; `add_node` returns a stable graph-local handle. `node_at` uses insertion order and `find_node` locates a value. Reject foreign/invalid handles and non-finite weights. Fresh cells are clear. Undirected mutations preserve symmetry and weight. Duplicate adds and absent removes are clean no-ops. Neighbor iteration scans the full row. `as_graph_view()` exposes dynamic node lookup and weighted handle iteration without representation details.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- add_node O(N^2); add/remove/has O(1); neighbor iteration O(N); full traversal O(N^2); O(N^2) space.
