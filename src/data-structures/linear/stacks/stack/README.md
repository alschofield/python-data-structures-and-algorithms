# Stack

## Evidence-Based Contract

`stack.Stack` must be importable. The test scaffold names `push(item)`, `pop()`, `peek()`, `size`, and `isEmpty`.

## Boundaries To Specify In Tests

- Constructor behavior; whether `size` and `isEmpty` are properties or methods; return values; empty-operation behavior; mutation; retained object references; accepted runtime types; and raised exceptions are not specified.
- The scaffold has no Python type annotations. Type hints, if added, are not runtime validation unless the implementation explicitly validates values.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/data-structures/linear/stacks/stack`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
