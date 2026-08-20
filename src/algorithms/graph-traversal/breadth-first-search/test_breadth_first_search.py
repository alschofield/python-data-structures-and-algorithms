import pytest

from breadth_first_search import breadthFirstSearch


def test_breadth_first_search_exports_required_api():
    assert breadthFirstSearch is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_breadth_first_search_contract_scaffold():
    pytest.fail("Implement and expand tests for: breadthFirstSearch(graph, source): number[] | undefined")
