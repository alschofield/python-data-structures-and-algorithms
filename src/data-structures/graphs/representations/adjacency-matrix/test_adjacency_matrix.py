import pytest

from adjacency_matrix import AdjacencyMatrix


def test_adjacency_matrix_exports_required_api():
    assert AdjacencyMatrix is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_adjacency_matrix_contract_scaffold():
    pytest.fail("Implement and expand tests for: constructor(vertexCount, directed), addEdge(from, to), removeEdge(from, to), hasEdge(from, to), neighbors(vertex), vertexCount, edgeCount")
