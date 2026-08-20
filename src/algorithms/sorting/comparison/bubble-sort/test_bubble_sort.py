import pytest

from bubble_sort import bubbleSort


def test_bubble_sort_exports_required_api():
    assert bubbleSort is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_bubble_sort_contract_scaffold():
    pytest.fail("Implement and expand tests for: bubbleSort(items, compare): boolean | void")
