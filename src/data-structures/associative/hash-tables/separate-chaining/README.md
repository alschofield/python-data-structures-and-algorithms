# Separate-Chaining Hash Table

## How It Works

A hash selects a bucket and each collision bucket is a linked chain. `set`
preserves the chosen fixed capacity; `set_resizing` doubles and rehashes
buckets before a new entry would exceed a 0.75 load factor.

## Required API

Implement HashTable<K, V> with: constructor(initial_capacity, hash, equals),
set(key, value), set_resizing(key, value), get(key), remove(key), contains(key),
size, capacity, is_empty. Use idiomatic Python classes/functions, type hints,
and return values; the required operations remain equivalent to the canonical C
curriculum.

## Contract

- `initial_capacity` must be nonzero. Standard callers use `10`; reject an
  invalid capacity without creating a table. Keys must not be null; values may
  be null.
- Both set methods insert a new key or replace an equal key's value while
  retaining the first stored key. `set` never changes capacity.
- `set_resizing` checks whether adding a new key would exceed a 0.75 load
  factor. If so, double capacity and rehash every entry with
  `hash(key) % new_capacity` before insertion. A failed growth preserves the
  table, capacity, and result.
- Absent/null-key lookups and removals do not mutate. Collisions must work.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- set/get/remove/contains expected O(1) with short chains, O(n / capacity) as
  fixed chains grow, O(n) worst case; set_resizing amortized O(1), O(n) when
  resizing; size/capacity/is_empty O(1); O(entries + capacity) space.
