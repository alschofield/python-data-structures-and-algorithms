# A-Star

## Evidence-Based Contract

`a_star.aStar` must be importable. The test scaffold names `aStar(graph: GraphView, source, goal: int, heuristic) -> list[int] | None` and requires weighted neighbors.

## Boundaries To Specify In Tests

- Source typing, path ordering, graph mutation, source and goal validation, heuristic calling convention, weight domain, reference behavior, and raised exceptions are not specified.
- `GraphView` and weighted-neighbor iteration are required by name only; their import paths, shapes, and runtime validation behavior are not specified.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/algorithms/shortest-paths/a-star`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
