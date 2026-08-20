import pytest

from queue import Queue


def test_queue_exports_required_api():
    assert Queue is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_queue_contract_scaffold():
    pytest.fail("Implement and expand tests for: enqueue(item), dequeue(), peek(), size, isEmpty")
