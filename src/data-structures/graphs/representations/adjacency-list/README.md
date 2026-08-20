# Adjacency List

## How It Works

One outgoing-edge collection per dense vertex index; the sparse graph representation.

## Required API

Implement AdjacencyList with: constructor(vertexCount, directed), addEdge(from, to), hasEdge(from, to), neighbors(vertex), vertexCount, edgeCount. Use idiomatic Python classes/functions, type hints, and return values; the required operations remain equivalent to the canonical C curriculum.

## Contract

- Reject vertices outside [0, vertexCount). Directedness is fixed at construction; undirected edges are stored in both directions. Choose and document duplicate policy, allow self-loops unless documented otherwise, and return neighbors in deterministic order.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- addEdge amortized O(1); hasEdge and neighbor iteration O(deg(u)); full traversal O(V + E); O(V + E) space.
