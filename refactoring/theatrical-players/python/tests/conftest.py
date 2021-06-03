import json

import pytest
from approvaltests.utils import get_adjacent_file


def load_json(file_name: str):
    with open(get_adjacent_file(file_name)) as f:
        return json.loads(f.read())


@pytest.fixture
def invoice():
    return load_json("invoice.json")


@pytest.fixture
def plays():
    return load_json("plays.json")


@pytest.fixture
def invoice_new_plays():
    return load_json("invoice_new_plays.json")


@pytest.fixture
def new_plays():
    return load_json("new_plays.json")
