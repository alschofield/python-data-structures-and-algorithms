# Prefix Trie

## Evidence-Based Contract

`prefix_trie.PrefixTrie` must be importable. The test scaffold names `insert(key)`, `contains(key)`, `startsWith(prefix)`, `remove(key)`, and `size`.

## Boundaries To Specify In Tests

- Constructor behavior; whether `size` is a property or method; key and prefix domains; return values; duplicate and absent-key behavior; mutation; retained string or object references; accepted runtime types; and raised exceptions are not specified.
- The scaffold has no Python type annotations. Type hints, if added, are not runtime validation unless the implementation explicitly validates values.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/data-structures/trees/tries/prefix-trie`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
