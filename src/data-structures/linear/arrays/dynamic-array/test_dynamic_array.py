import pytest

from dynamic_array import DynamicArray


def test_dynamic_array_exports_required_api():
    assert DynamicArray is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_dynamic_array_contract_scaffold():
    pytest.fail("Implement and expand tests for: create(), get(index), set(index, item), insert(index, item), remove(index), size, capacity, isEmpty")
