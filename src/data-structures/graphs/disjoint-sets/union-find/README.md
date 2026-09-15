# Union-Find

## Evidence-Based Contract

`union_find.UnionFind` must be importable. The test scaffold names `constructor(elementCount)`, `find(element)`, `union(a, b)`, `connected(a, b)`, and `setCount`.

## Boundaries To Specify In Tests

- Python constructor spelling, valid element-index range, representatives and return values, whether `setCount` is a property or method, mutation, accepted runtime types, and raised exceptions are not specified.
- The scaffold has no Python type annotations. Type hints, if added, are not runtime validation unless the implementation explicitly validates values.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/data-structures/graphs/disjoint-sets/union-find`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
