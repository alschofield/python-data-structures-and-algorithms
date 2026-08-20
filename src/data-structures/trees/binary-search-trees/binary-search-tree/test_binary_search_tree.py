import pytest

from binary_search_tree import BinarySearchTree


def test_binary_search_tree_exports_required_api():
    assert BinarySearchTree is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_binary_search_tree_contract_scaffold():
    pytest.fail("Implement and expand tests for: constructor(compare), insert(item), find(key), contains(key), remove(key), inOrder(visitor), size, isEmpty")
