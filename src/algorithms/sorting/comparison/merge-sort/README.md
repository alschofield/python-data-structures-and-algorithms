# Merge Sort

## How It Works

Recursively sort halves, then merge them through an auxiliary buffer.

## Required API

Implement mergeSort<T> with: mergeSort(items, compare): boolean | void. Use idiomatic Python classes/functions, type hints, and return values; the required operations remain equivalent to the canonical C curriculum.

## Contract

- Sort ascending and stable by taking the left run on ties. Use an O(n) auxiliary buffer. If allocation can fail in the implementation environment, failure must preserve input. Do not use built-in sorting.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- best/average/worst O(n log n), O(n) auxiliary plus O(log n) recursion space.
