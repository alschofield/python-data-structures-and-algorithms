import pytest

from stack import Stack


def test_stack_exports_required_api():
    assert Stack is not None


@pytest.mark.xfail(reason="Production API is user-owned and has not been written.")
def test_stack_contract_scaffold():
    pytest.fail("Implement and expand tests for: push(item), pop(), peek(), size, isEmpty")
