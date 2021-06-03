import pytest
from approvaltests import verify

from statement.statement import statement


def test_example_statement(invoice, plays):
    verify(statement(invoice, plays))


def test_statement_with_new_play_types(invoice_new_plays, new_plays):
    with pytest.raises(ValueError) as exception_info:
        statement(invoice_new_plays, new_plays)
    assert "unknown type" in str(exception_info.value)
