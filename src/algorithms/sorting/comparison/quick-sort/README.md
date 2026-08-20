# Quick Sort

## How It Works

Partition around a defensively chosen pivot, then recursively sort both partitions.

## Required API

Implement quickSort<T> with: quickSort(items, compare): boolean | void. Use idiomatic Python classes/functions, type hints, and return values; the required operations remain equivalent to the canonical C curriculum.

## Contract

- Sort in place ascending; stability is not required. Use median-of-three or randomized pivots, not a fixed first/last pivot. All-equal and duplicate inputs must remain correct. Do not use built-in sorting.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- best/average O(n log n), worst O(n^2), expected O(log n) recursion space.
