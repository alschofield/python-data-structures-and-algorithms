# Radix Sort

## How It Works

Use stable least-significant-digit counting passes in a fixed radix.

## Required API

Implement radixSort with: radixSort(items): boolean | void. Use idiomatic Python classes/functions, type hints, and return values; the required operations remain equivalent to the canonical C curriculum.

## Contract

- Process digits least to most significant. Every digit pass must be stable; preserve overall stability. Do not use built-in sorting.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- best/average/worst O(d(n + k)), O(n + k) auxiliary space.
