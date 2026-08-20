import pytest

from heap_sort import heapSort


def test_heap_sort_exports_required_api():
    assert heapSort is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_heap_sort_contract_scaffold():
    pytest.fail("Implement and expand tests for: heapSort(items, compare): boolean | void")
