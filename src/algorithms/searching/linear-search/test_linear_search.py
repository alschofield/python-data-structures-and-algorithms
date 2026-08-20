import pytest

from linear_search import linearSearch


def test_linear_search_exports_required_api():
    assert linearSearch is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_linear_search_contract_scaffold():
    pytest.fail("Implement and expand tests for: linearSearch(items, key, compare): number | undefined")
