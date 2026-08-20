import pytest

from quick_sort import quickSort


def test_quick_sort_exports_required_api():
    assert quickSort is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_quick_sort_contract_scaffold():
    pytest.fail("Implement and expand tests for: quickSort(items, compare): boolean | void")
