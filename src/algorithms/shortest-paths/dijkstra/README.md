# Dijkstra

## How It Works

Repeatedly settle the lowest tentative distance and relax its non-negative weighted outgoing edges.

## Required API

Implement dijkstra with: dijkstra(graph, source): { distances, parents } | undefined. Use idiomatic Python classes/functions, type hints, and return values; the required operations remain equivalent to the canonical C curriculum.

## Contract

- Reject negative weights and invalid sources. Unreachable vertices use explicit infinity. Parent links reconstruct shortest paths. Support cycles, parallel edges, and self-loops. Do not use a library priority queue.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- O((V + E) log V) time with a binary heap and O(V) auxiliary space.
