# Dijkstra

## Evidence-Based Contract

`dijkstra.dijkstra` must be importable. The test scaffold names `dijkstra(graph: GraphView, source: int) -> DijkstraResult` with index-keyed outputs and weighted neighbors.

## Boundaries To Specify In Tests

- The `DijkstraResult` members, distance representation, graph mutation, source-index validation, weight domain, reference behavior, and raised exceptions are not specified.
- `GraphView` and weighted-neighbor iteration are required by name only; their import paths, shapes, and runtime validation behavior are not specified.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/algorithms/shortest-paths/dijkstra`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
