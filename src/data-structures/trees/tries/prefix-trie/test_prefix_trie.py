import pytest

from prefix_trie import PrefixTrie


def test_prefix_trie_exports_required_api():
    assert PrefixTrie is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_prefix_trie_contract_scaffold():
    pytest.fail("Implement and expand tests for: insert(key), contains(key), startsWith(prefix), remove(key), size")
