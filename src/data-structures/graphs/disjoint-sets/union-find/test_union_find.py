import pytest

from union_find import UnionFind


def test_union_find_exports_required_api():
    assert UnionFind is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_union_find_contract_scaffold():
    pytest.fail("Implement and expand tests for: constructor(elementCount), find(element), union(a, b), connected(a, b), setCount")
