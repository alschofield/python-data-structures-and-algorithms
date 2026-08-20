import pytest

from doubly_linked_list import DoublyLinkedList


def test_doubly_linked_list_exports_required_api():
    assert DoublyLinkedList is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_doubly_linked_list_contract_scaffold():
    pytest.fail("Implement and expand tests for: pushFront(item), pushBack(item), popFront(), popBack(), get(index), insert(index, item), remove(index), size, isEmpty")
