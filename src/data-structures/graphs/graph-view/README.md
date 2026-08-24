# GraphView

## Required API

Implement `GraphView` as a Protocol or abstract base class with `vertex_count` and `neighbors(vertex: int) -> Iterable[tuple[int, int]]`.

## Contract

- Vertexes are dense indexes in `range(vertex_count)`. Neighbor iteration rejects out-of-range indexes, yields each outgoing weighted edge once in deterministic order, and does not mutate the backing graph.
- Weights are nonnegative. Adjacency-list, adjacency-matrix, and imported-graph adapters map their storage to vertex indexes. GraphView never exposes node handles or values.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- `vertex_count` is O(1). Neighbor iteration is O(deg(u)) for an adjacency list and O(N) for an adjacency matrix.
