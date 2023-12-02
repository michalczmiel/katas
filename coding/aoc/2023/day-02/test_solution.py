import pytest

from solution import Game, GameSet


def test_game_from_str():
    game_str = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

    expected_game = Game(
        id=1,
        sets=[
            GameSet(blue=3, red=4),
            GameSet(red=1, green=2, blue=6),
            GameSet(green=2),
        ],
    )

    game = Game.from_str(game_str)

    assert game.id == expected_game.id
    assert game.sets == expected_game.sets
