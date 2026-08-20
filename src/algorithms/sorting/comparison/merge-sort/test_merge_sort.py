import pytest

from merge_sort import mergeSort


def test_merge_sort_exports_required_api():
    assert mergeSort is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_merge_sort_contract_scaffold():
    pytest.fail("Implement and expand tests for: mergeSort(items, compare): boolean | void")
