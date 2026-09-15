# Linear Search

## Evidence-Based Contract

`linear_search.linearSearch` must be importable. The current test scaffold names `linearSearch(items, key, compare): number | undefined` and provides no executable behavioral cases.

## Boundaries To Specify In Tests

- Mutation of `items`, reference/identity behavior for items and `key`, accepted runtime types, comparator convention, missing-result representation, and raised exceptions are not specified.
- The scaffold has no Python type annotations. Type hints, if added, are not runtime validation unless the implementation explicitly validates values.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/algorithms/searching/linear-search`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
