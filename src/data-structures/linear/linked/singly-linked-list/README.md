# Singly Linked List

## Evidence-Based Contract

`singly_linked_list.SinglyLinkedList` must be importable. The test scaffold names `pushFront(item)`, `pushBack(item)`, `popFront()`, `popBack()`, `get(index)`, `insert(index, item)`, `remove(index)`, `size`, and `isEmpty`.

## Boundaries To Specify In Tests

- Constructor behavior; whether `size` and `isEmpty` are properties or methods; index rules; return values; failure atomicity; mutation; retained item references; accepted runtime types; and raised exceptions are not specified.
- The scaffold has no Python type annotations. Type hints, if added, are not runtime validation unless the implementation explicitly validates values.
- No complexity target is currently verified or specified.

## Verification

Run `python -m pytest src/data-structures/linear/linked/singly-linked-list`. The import check must pass; the behavior scaffold is intentionally marked xfail until concrete tests are written.
