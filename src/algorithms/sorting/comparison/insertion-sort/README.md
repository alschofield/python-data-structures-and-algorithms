# Insertion Sort

## How It Works

Grow a sorted prefix by shifting strictly greater items right for each next item.

## Required API

Implement insertionSort<T> with: insertionSort(items, compare): boolean | void. Use idiomatic Python classes/functions, type hints, and return values; the required operations remain equivalent to the canonical C curriculum.

## Contract

- Sort in place ascending and stable: equal items retain their order. Nearly sorted input must be adaptive. Do not use built-in sorting.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- best O(n), average/worst O(n^2), O(1) extra space.
