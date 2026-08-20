import pytest

from radix_sort import radixSort


def test_radix_sort_exports_required_api():
    assert radixSort is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_radix_sort_contract_scaffold():
    pytest.fail("Implement and expand tests for: radixSort(items): boolean | void")
