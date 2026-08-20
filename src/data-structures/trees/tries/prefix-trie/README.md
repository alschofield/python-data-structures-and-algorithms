# Prefix Trie

## How It Works

A character tree where root-to-node paths spell prefixes and marked nodes spell stored keys.

## Required API

Implement PrefixTrie with: insert(key), contains(key), startsWith(prefix), remove(key), size. Use idiomatic Python classes/functions, type hints, and return values; the required operations remain equivalent to the canonical C curriculum.

## Contract

- Duplicate insertion is idempotent. contains matches whole keys; startsWith accepts the empty prefix. remove fails cleanly for absent keys and prunes only now-unused nodes. Do not use a library trie/map for child storage.
- Implement from first principles. Do not substitute dict, set, built-in sorting/searching, heapq, or collections.deque for the exercise.

## Complexity Targets

- insert, contains, startsWith, remove O(m) for key length; O(total stored characters) space in the worst case.
