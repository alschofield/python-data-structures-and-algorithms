import pytest

from depth_first_search import depthFirstSearch


def test_depth_first_search_exports_required_api():
    assert depthFirstSearch is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_depth_first_search_contract_scaffold():
    pytest.fail("Implement and expand tests for: depthFirstSearch(graph, source): number[] | undefined")
