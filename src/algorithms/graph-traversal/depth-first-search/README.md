# Depth-First Search

## How It Works

Traverse any GraphView as far as possible down each branch before backtracking, using a stack or recursion.

## Required API

Implement `depthFirstSearch(graph: GraphView[T], source: NodeHandle) -> list[NodeHandle] | None`.

## Contract

- Visit each reachable node once using a visited-handle structure, leave graph unchanged, reject invalid or foreign source handles, and handle cycles, self-loops, and disconnected graphs. Accept dynamic GraphView adapters and ignore every edge weight. Return handles in visit order. Understand both recursive and explicit-stack forms; do not use a library stack.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- O(V + E) time and O(V) auxiliary space.
