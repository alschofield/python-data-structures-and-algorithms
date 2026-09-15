# Binary Search

## Evidence-Based Contract

`binary_search.binarySearch` must be importable. The current test scaffold names `binarySearch(items, key, compare): number | undefined` and provides no executable behavioral cases.

## Boundaries To Specify In Tests

- Required ordering of `items`, mutation of `items`, duplicate-result selection, reference/identity behavior, comparator convention, missing-result representation, and raised exceptions are not specified.
- The scaffold has no Python type annotations. Type hints, if added, are not runtime validation unless the implementation explicitly validates values.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/algorithms/searching/binary-search`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
