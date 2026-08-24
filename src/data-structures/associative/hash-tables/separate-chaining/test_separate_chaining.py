import pytest

from separate_chaining import HashTable


def test_separate_chaining_exports_required_api():
    assert HashTable is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_separate_chaining_contract_scaffold():
    pytest.fail(
        "Implement and expand tests for: constructor(initial_capacity, hash, equals), "
        "set(key, value), set_resizing(key, value), get(key), remove(key), "
        "contains(key), size, capacity, is_empty; reject zero capacity; keep "
        "set capacity fixed; double and rehash before set_resizing exceeds 0.75 load"
    )
