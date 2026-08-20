import pytest

from binary_search import binarySearch


def test_binary_search_exports_required_api():
    assert binarySearch is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_binary_search_contract_scaffold():
    pytest.fail("Implement and expand tests for: binarySearch(items, key, compare): number | undefined")
