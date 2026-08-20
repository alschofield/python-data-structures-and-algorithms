import pytest

from resizable_separate_chaining import ResizableHashTable


def test_resizable_separate_chaining_exports_required_api():
    assert ResizableHashTable is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_resizable_separate_chaining_contract_scaffold():
    pytest.fail("Implement and expand tests for: constructor(hash, equals), set(key, value), get(key), remove(key), contains(key), size, capacity, isEmpty")
