import pytest

from solution import Card


def test_card_from_str():
    raw = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"

    expected = Card(
        id="1",
        winning_numbers={"41", "48", "83", "86", "17"},
        numbers={"83", "86", "6", "31", "17", "9", "48", "53"},
    )

    card = Card.from_str(raw)

    assert card == expected


def test_card_points_with_three_matches():
    card = Card(
        id="1",
        winning_numbers={"41", "48", "83", "86", "17"},
        numbers={"83", "86", "6", "31", "17", "9", "48", "53"},
    )

    assert card.points == 8


def test_card_points_with_no_matches():
    card = Card(
        id="1",
        winning_numbers={"41", "48", "83", "86", "17"},
        numbers={"1", "2", "3", "4"},
    )

    assert card.points == 0
