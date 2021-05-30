import json

import pytest
from approvaltests import verify
from approvaltests.utils import get_adjacent_file

from statement.statement import statement


@pytest.fixture
def invoice():
    with open(get_adjacent_file("invoice.json")) as f:
        return json.loads(f.read())


@pytest.fixture
def plays():
    with open(get_adjacent_file("plays.json")) as f:
        return json.loads(f.read())


@pytest.fixture
def invoice_new_plays():
    with open(get_adjacent_file("invoice_new_plays.json")) as f:
        return json.loads(f.read())


@pytest.fixture
def new_plays():
    with open(get_adjacent_file("new_plays.json")) as f:
        return json.loads(f.read())


def test_example_statement(invoice, plays):
    verify(statement(invoice, plays))


def test_statement_with_new_play_types(invoice_new_plays, new_plays):
    with pytest.raises(ValueError) as exception_info:
        statement(invoice_new_plays, new_plays)
    assert "unknown type" in str(exception_info.value)
