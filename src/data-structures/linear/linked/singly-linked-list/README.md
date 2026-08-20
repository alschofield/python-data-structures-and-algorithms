# Singly Linked List

## How It Works

A node chain with one forward link and a head pointer.

## Required API

Implement SinglyLinkedList<T> with: pushFront(item), pushBack(item), popFront(), popBack(), get(index), insert(index, item), remove(index), size, isEmpty. Use idiomatic Python classes/functions, type hints, and return values; the required operations remain equivalent to the canonical C curriculum.

## Contract

- Indexes are [0, size); insert also accepts size. Failed operations preserve the list. Removing the final node leaves a valid empty list. Stored values remain caller-owned.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- pushFront, popFront, size, isEmpty O(1); all other operations O(n); O(n) nodes with one link each.
