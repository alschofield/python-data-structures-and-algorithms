import pytest

from insertion_sort import insertionSort


def test_insertion_sort_exports_required_api():
    assert insertionSort is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_insertion_sort_contract_scaffold():
    pytest.fail("Implement and expand tests for: insertionSort(items, compare): boolean | void")
