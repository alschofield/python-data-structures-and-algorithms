# Adjacency List

## How It Works

One weighted outgoing-edge collection per dynamically added node; the sparse graph representation.

## Required API

Implement `AdjacencyList[T]` with: `create(directed)`, `add_node(value) -> NodeHandle`, `find_node(value) -> NodeHandle | None`, `node_at(index) -> NodeHandle | None`, `node_value(node) -> T | None`, `add_edge(from_node, to_node, weight)`, `has_edge`, `neighbors(node)`, `node_count`, `edge_count`, and `as_graph_view() -> GraphView[T]`. `neighbors(node)` yields deterministic `(NodeHandle, weight)` edges.

## Contract

- `create` starts empty; `add_node` returns a stable graph-local handle. `node_at` uses insertion order and `find_node` locates a value. Reject foreign/invalid handles and non-finite weights. Directedness is fixed at creation; undirected edges are stored in both directions with the same weight. Reject duplicate edges, allow self-loops and negative weights, and return neighbors in deterministic insertion order. `as_graph_view()` exposes dynamic node lookup and weighted handle iteration without representation details.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- add_node and add_edge amortized O(1); has_edge and neighbor iteration O(deg(u)); full traversal O(V + E); O(V + E) space.
