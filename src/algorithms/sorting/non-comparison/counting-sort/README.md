# Counting Sort

## How It Works

Count keys in [0, keyLimit), prefix-sum their positions, and place items in a stable output buffer.

## Required API

Implement countingSort with: countingSort(items, keyLimit): boolean | void. Use idiomatic Python classes/functions, type hints, and return values; the required operations remain equivalent to the canonical C curriculum.

## Contract

- Use no element comparisons. Validate keys against the declared range. Keep equal keys stable by reverse input placement or equivalent. Do not use built-in sorting.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- best/average/worst O(n + k), O(n + k) auxiliary space.
