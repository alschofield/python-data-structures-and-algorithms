# Separate-Chaining Hash Table

## Evidence-Based Contract

`separate_chaining.HashTable` must be importable. The test scaffold names `constructor(initial_capacity, hash, equals)`, `set(key, value)`, `set_resizing(key, value)`, `get(key)`, `remove(key)`, `contains(key)`, `size`, `capacity`, and `is_empty`.

## Required Behavior From The Scaffold

- Zero capacity is rejected. `set` keeps capacity fixed.
- Before `set_resizing` would exceed a 0.75 load, capacity doubles and entries are rehashed.

## Boundaries To Specify In Tests

- Python constructor spelling; hash and equality callback conventions; return values; duplicate-key policy; mutation and failure atomicity; key and value reference behavior; whether `size`, `capacity`, and `is_empty` are properties or methods; accepted runtime types; and exception classes are not specified.
- The scaffold has no Python type annotations. Type hints, if added, are not runtime validation unless the implementation explicitly validates values.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/data-structures/associative/hash-tables/separate-chaining`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
