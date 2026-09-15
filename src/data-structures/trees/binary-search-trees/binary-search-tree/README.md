# Binary Search Tree

## Evidence-Based Contract

`binary_search_tree.BinarySearchTree` must be importable. The test scaffold names `constructor(compare)`, `insert(item)`, `find(key)`, `contains(key)`, `remove(key)`, `inOrder(visitor)`, `size`, and `isEmpty`.

## Boundaries To Specify In Tests

- Python constructor spelling, comparator convention, duplicate handling, return values, visitor semantics, mutation and failure atomicity, retained object references, accepted runtime types, and raised exceptions are not specified.
- The scaffold has no Python type annotations. Type hints, if added, are not runtime validation unless the implementation explicitly validates values.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/data-structures/trees/binary-search-trees/binary-search-tree`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
