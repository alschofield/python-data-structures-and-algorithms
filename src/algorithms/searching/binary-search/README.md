# Binary Search

## How It Works

An iterative range-halving search over input already sorted ascending by compare.

## Required API

Implement binarySearch<T> with: binarySearch(items, key, compare): number | undefined. Use idiomatic Python classes/functions, type hints, and return values; the required operations remain equivalent to the canonical C curriculum.

## Contract

- Assume but do not sort or validate the order. Return any matching duplicate index, undefined when missing, and never modify input. Midpoint logic must always shrink safely.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- best O(1), average/worst O(log n), O(1) extra space.
