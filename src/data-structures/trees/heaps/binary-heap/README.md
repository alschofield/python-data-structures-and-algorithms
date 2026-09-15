# Binary Heap

## Evidence-Based Contract

`binary_heap.BinaryHeap` must be importable. The test scaffold names `constructor(compare)`, `push(item)`, `pop()`, `peek()`, `size`, and `isEmpty`.

## Boundaries To Specify In Tests

- Python constructor spelling, comparator convention and priority direction, return values, empty-operation behavior, mutation, retained item references, accepted runtime types, and raised exceptions are not specified.
- The scaffold has no Python type annotations. Type hints, if added, are not runtime validation unless the implementation explicitly validates values.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/data-structures/trees/heaps/binary-heap`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
