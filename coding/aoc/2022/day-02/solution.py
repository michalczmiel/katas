from typing import List, Tuple

ROCK = 1
PAPER = 2
SCISSORS = 3

WIN_SCORE = 6
DRAW_SCORE = 3

LOOSE = 1
DRAW = 2
WIN = 3

OPPONENT_SHAPE_MAPPING = {"A": ROCK, "B": PAPER, "C": SCISSORS}
PLAYER_SHAPE_MAPPING = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}
SUGGESTED_MOVE_SHAPE_MAPPING = {"X": LOOSE, "Y": DRAW, "Z": WIN}


def read_input(file_name: str) -> List[Tuple[int]]:
    shapes = []

    with open(file_name) as file:
        for line in file:
            opponent, player = line.strip().split(" ")
            shapes.append((opponent, player))
    return shapes


def get_total_score_based_on_first_strategy(shapes: List[Tuple[str]]) -> int:
    total_score = 0

    for opponent_shape, player_shape in shapes:
        opponent_move = OPPONENT_SHAPE_MAPPING[opponent_shape]
        player_move = PLAYER_SHAPE_MAPPING[player_shape]

        if opponent_move == ROCK:
            if player_move == ROCK:
                round_score = player_move + DRAW_SCORE
            elif player_move == PAPER:
                round_score = player_move + WIN_SCORE
            else:
                round_score = player_move
        elif opponent_move == PAPER:
            if player_move == ROCK:
                round_score = player_move
            elif player_move == PAPER:
                round_score = player_move + DRAW_SCORE
            else:
                round_score = player_move + WIN_SCORE
        else:
            if player_move == ROCK:
                round_score = player_move + WIN_SCORE
            elif player_move == PAPER:
                round_score = player_move
            else:
                round_score = player_move + DRAW_SCORE

        total_score += round_score

    return total_score


def get_total_score_based_on_second_strategy(shapes: List[Tuple[str]]) -> int:
    total_score = 0

    for opponent_shape, player_shape in shapes:
        opponent_move = OPPONENT_SHAPE_MAPPING[opponent_shape]
        player_suggested_move = SUGGESTED_MOVE_SHAPE_MAPPING[player_shape]

        if opponent_move == ROCK:
            if player_suggested_move == LOOSE:
                round_score = SCISSORS
            elif player_suggested_move == DRAW:
                round_score = ROCK + DRAW_SCORE
            else:
                round_score = PAPER + WIN_SCORE
        elif opponent_move == PAPER:
            if player_suggested_move == LOOSE:
                round_score = ROCK
            elif player_suggested_move == DRAW:
                round_score = PAPER + DRAW_SCORE
            else:
                round_score = SCISSORS + WIN_SCORE
        else:
            if player_suggested_move == LOOSE:
                round_score = PAPER
            elif player_suggested_move == DRAW:
                round_score = SCISSORS + DRAW_SCORE
            else:
                round_score = ROCK + WIN_SCORE

        total_score += round_score

    return total_score


def solution() -> None:
    """Solution to https://adventofcode.com/2022/day/2"""

    print(get_total_score_based_on_first_strategy(read_input("input.txt")))
    print(get_total_score_based_on_second_strategy(read_input("input.txt")))


if __name__ == "__main__":
    solution()
