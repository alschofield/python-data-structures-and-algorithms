import pytest

from a_star import aStar


def test_a_star_exports_required_api():
    assert aStar is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_a_star_contract_scaffold():
    pytest.fail("Implement and expand tests for: aStar(graph: GraphView, source, goal: int, heuristic) -> list[int] | None using weighted neighbors")
