# Dijkstra

## How It Works

Repeatedly settle the lowest tentative distance and relax its non-negative weighted outgoing edges.

## Required API

Implement `dijkstra(graph: GraphView[T], source: NodeHandle) -> DijkstraResult | None`, where `DijkstraResult` exposes `distance(node) -> float | None` and `parent(node) -> NodeHandle | None`.

## Contract

- Consume dynamic GraphView weighted neighbors to relax edges. Reject negative weights and invalid or foreign source handles. Unreachable nodes have no distance. Parent handles reconstruct shortest paths. Support cycles, parallel edges, and self-loops. Do not use a library priority queue.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- O((V + E) log V) time with a binary heap and O(V) auxiliary space.
