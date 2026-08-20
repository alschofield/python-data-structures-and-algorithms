# Breadth-First Search

## How It Works

Traverse an adjacency list level by level using a FIFO frontier.

## Required API

Implement breadthFirstSearch with: breadthFirstSearch(graph, source): number[] | undefined. Use idiomatic Python classes/functions, type hints, and return values; the required operations remain equivalent to the canonical C curriculum.

## Contract

- Mark vertices visited when enqueued. Visit each reachable vertex once, leave graph unchanged, reject invalid source, and handle cycles, self-loops, and disconnected graphs. Do not use a library queue.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- O(V + E) time and O(V) auxiliary space with an adjacency list.
