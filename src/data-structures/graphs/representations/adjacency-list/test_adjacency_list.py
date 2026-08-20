import pytest

from adjacency_list import AdjacencyList


def test_adjacency_list_exports_required_api():
    assert AdjacencyList is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_adjacency_list_contract_scaffold():
    pytest.fail("Implement and expand tests for: constructor(vertexCount, directed), addEdge(from, to), hasEdge(from, to), neighbors(vertex), vertexCount, edgeCount")
