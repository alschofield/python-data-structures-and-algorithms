# A-Star

## How It Works

Order the frontier by g(n) + h(n), cost so far plus an admissible remaining-cost estimate.

## Required API

Implement aStar with: aStar(graph, source, goal, heuristic): number[] | undefined. Use idiomatic Python classes/functions, type hints, and return values; the required operations remain equivalent to the canonical C curriculum.

## Contract

- Require non-negative weights. With zero heuristic, match Dijkstra behavior. Resolve frontier ties deterministically, return an optimal source-to-goal path for admissible heuristics, and return undefined when unreachable. Do not use a library priority queue.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- Worst case O((V + E) log V) time and O(V) auxiliary space.
