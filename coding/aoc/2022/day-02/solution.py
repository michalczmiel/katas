from typing import List

ROCK = 1
PAPER = 2
SCISSORS = 3

WIN_SCORE = 6
DRAW_SCORE = 3

OPPONENT_SHAPE_MAPPING = {"A": ROCK, "B": PAPER, "C": SCISSORS}
PLAYER_SHAPE_MAPPING = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}


def read_input(file_name: str) -> List:
    moves = []

    with open(file_name) as file:
        for line in file:
            opponent, player = line.strip().split(" ")
            moves.append(
                (OPPONENT_SHAPE_MAPPING[opponent], PLAYER_SHAPE_MAPPING[player])
            )

    return moves


def get_total_score_base_on_strategy(moves: List[List[str]]) -> int:
    total_score = 0

    for opponent_move, player_move in moves:
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


def solution() -> None:
    """Solution to https://adventofcode.com/2022/day/2"""

    print(get_total_score_base_on_strategy(read_input("input.txt")))


if __name__ == "__main__":
    solution()
