# Breadth-First Search

## Evidence-Based Contract

`breadth_first_search.breadthFirstSearch` must be importable. The test scaffold names `breadthFirstSearch(graph: GraphView, source: int) -> list[int] | None` and says to ignore edge weights.

## Boundaries To Specify In Tests

- Traversal order, graph mutation, source-index validation, unreachable-result semantics, reference behavior, and raised exceptions are not specified.
- `GraphView` is a runtime dependency named by the scaffold; no import path, protocol shape, or runtime validation behavior is specified here.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/algorithms/graph-traversal/breadth-first-search`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
