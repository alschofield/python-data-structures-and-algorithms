import pytest

from counting_sort import countingSort


def test_counting_sort_exports_required_api():
    assert countingSort is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_counting_sort_contract_scaffold():
    pytest.fail("Implement and expand tests for: countingSort(items, keyLimit): boolean | void")
