import pytest

from adjacency_matrix import AdjacencyMatrix


def test_adjacency_matrix_exports_required_api():
    assert AdjacencyMatrix is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_adjacency_matrix_contract_scaffold():
    pytest.fail("Implement and expand tests for: create(directed), add_node(value), stable dense indexes, handle-based weighted edges, and GraphView index adaptation")
