# A-Star

## How It Works

Order the frontier by g(n) + h(n), cost so far plus an admissible remaining-cost estimate.

## Required API

Implement `aStar(graph: GraphView[T], source: NodeHandle, goal: NodeHandle, heuristic: Callable[[NodeHandle], float]) -> list[NodeHandle] | None`.

## Contract

- Consume dynamic GraphView weighted neighbors. Reject invalid or foreign source/goal handles and require non-negative weights. With zero heuristic, match Dijkstra behavior. Resolve frontier ties deterministically, return an optimal source-to-goal handle path for admissible heuristics, and return None when unreachable. Do not use a library priority queue.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- Worst case O((V + E) log V) time and O(V) auxiliary space.
