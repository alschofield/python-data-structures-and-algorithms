# Adjacency Matrix

## Evidence-Based Contract

`adjacency_matrix.AdjacencyMatrix` must be importable. The test scaffold names `create(directed)`, `add_node(value)`, stable dense indexes, handle-based weighted edges, and GraphView index adaptation.

## Boundaries To Specify In Tests

- Python constructor or factory spelling, node-handle type and lifetime, edge-operation names and return values, directed-edge behavior, mutation, index and handle validation, weight domain, retained value references, and raised exceptions are not specified.
- `GraphView` adaptation is required by name only; its import path, protocol shape, dynamic behavior, and runtime validation are not specified.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/data-structures/graphs/representations/adjacency-matrix`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
