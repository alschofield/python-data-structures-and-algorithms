# Adjacency Matrix

## How It Works

A single V by V edge grid indexed by vertex pair; the dense graph representation.

## Required API

Implement AdjacencyMatrix with: constructor(vertexCount, directed), addEdge(from, to), removeEdge(from, to), hasEdge(from, to), neighbors(vertex), vertexCount, edgeCount. Use idiomatic Python classes/functions, type hints, and return values; the required operations remain equivalent to the canonical C curriculum.

## Contract

- Reject out-of-range vertices. Fresh cells are clear. Undirected mutations preserve symmetry. Duplicate adds and absent removes are clean no-ops with documented return values. Neighbor iteration scans the full row.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- add/remove/has O(1); neighbor iteration O(V); full traversal O(V^2); O(V^2) space.
