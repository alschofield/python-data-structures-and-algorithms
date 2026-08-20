import pytest

from selection_sort import selectionSort


def test_selection_sort_exports_required_api():
    assert selectionSort is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_selection_sort_contract_scaffold():
    pytest.fail("Implement and expand tests for: selectionSort(items, compare): boolean | void")
