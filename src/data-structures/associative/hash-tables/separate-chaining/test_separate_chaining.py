import pytest

from separate_chaining import HashTable


def test_separate_chaining_exports_required_api():
    assert HashTable is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_separate_chaining_contract_scaffold():
    pytest.fail("Implement and expand tests for: constructor(hash, equals), set(key, value), get(key), remove(key), contains(key), size, isEmpty")
