# Heap Sort

## Evidence-Based Contract

`heap_sort.heapSort` must be importable. The current test scaffold names `heapSort(items, compare): boolean | void` and provides no executable behavioral cases.

## Boundaries To Specify In Tests

- Whether `items` is mutated, the return value, ordering direction, stability, reference/identity behavior, comparator convention, accepted runtime types, and raised exceptions are not specified.
- The scaffold has no Python type annotations. Type hints, if added, are not runtime validation unless the implementation explicitly validates values.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/algorithms/sorting/comparison/heap-sort`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
