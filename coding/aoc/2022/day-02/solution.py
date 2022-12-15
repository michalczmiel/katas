from typing import Iterator

ROCK = 1
PAPER = 2
SCISSORS = 3

WIN_SCORE = 6
DRAW_SCORE = 3
LOOSE_SCORE = 0

LOOSE = 1
DRAW = 2
WIN = 3

OPPONENT_SHAPE_MAPPING = {"A": ROCK, "B": PAPER, "C": SCISSORS}
PLAYER_SHAPE_MAPPING = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}
SUGGESTED_MOVE_SHAPE_MAPPING = {"X": LOOSE, "Y": DRAW, "Z": WIN}


def read_input(file_name: str) -> Iterator[tuple[str, str]]:
    with open(file_name) as file:
        for line in file:
            opponent, player = line.strip().split(" ")
            yield (opponent, player)


FIRST_STRATEGY = {
    ROCK: {ROCK: DRAW_SCORE, PAPER: WIN_SCORE, SCISSORS: LOOSE_SCORE},
    PAPER: {ROCK: LOOSE_SCORE, PAPER: DRAW_SCORE, SCISSORS: WIN_SCORE},
    SCISSORS: {ROCK: WIN_SCORE, PAPER: LOOSE_SCORE, SCISSORS: DRAW_SCORE},
}


def get_total_score_based_on_first_strategy(shapes: Iterator[tuple[str, str]]) -> int:
    total_score = 0

    for opponent_shape, player_shape in shapes:
        opponent_move = OPPONENT_SHAPE_MAPPING[opponent_shape]
        player_move = PLAYER_SHAPE_MAPPING[player_shape]
        total_score += player_move + FIRST_STRATEGY[opponent_move][player_move]

    return total_score


SECOND_STRATEGY = {
    ROCK: {LOOSE: SCISSORS, DRAW: ROCK + DRAW_SCORE, WIN: PAPER + WIN_SCORE},
    PAPER: {LOOSE: ROCK, DRAW: PAPER + DRAW_SCORE, WIN: SCISSORS + WIN_SCORE},
    SCISSORS: {LOOSE: PAPER, DRAW: SCISSORS + DRAW_SCORE, WIN: ROCK + WIN_SCORE},
}


def get_total_score_based_on_second_strategy(shapes: Iterator[tuple[str, str]]) -> int:
    total_score = 0

    for opponent_shape, player_shape in shapes:
        opponent_move = OPPONENT_SHAPE_MAPPING[opponent_shape]
        player_suggested_move = SUGGESTED_MOVE_SHAPE_MAPPING[player_shape]
        total_score += SECOND_STRATEGY[opponent_move][player_suggested_move]

    return total_score


def solution() -> None:
    """Solution to https://adventofcode.com/2022/day/2"""

    print(get_total_score_based_on_first_strategy(read_input("input.txt")))
    print(get_total_score_based_on_second_strategy(read_input("input.txt")))


if __name__ == "__main__":
    solution()
