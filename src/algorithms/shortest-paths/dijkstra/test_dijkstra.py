import pytest

from dijkstra import dijkstra


def test_dijkstra_exports_required_api():
    assert dijkstra is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_dijkstra_contract_scaffold():
    pytest.fail("Implement and expand tests for: dijkstra(graph: GraphView, source: int) -> DijkstraResult with index-keyed outputs and weighted neighbors")
