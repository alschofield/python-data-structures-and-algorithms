import pytest

from binary_heap import BinaryHeap


def test_binary_heap_exports_required_api():
    assert BinaryHeap is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_binary_heap_contract_scaffold():
    pytest.fail("Implement and expand tests for: constructor(compare), push(item), pop(), peek(), size, isEmpty")
