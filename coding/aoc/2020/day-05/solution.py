import math
from typing import NewType


BoardingPass = NewType("BoardingPass", str)
SeatId = NewType("SeatId", int)


def read_input() -> list[BoardingPass]:
    boarding_passes = []

    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            boarding_passes.append(line)

    return boarding_passes


def get_seat_id(boarding_pass: BoardingPass) -> SeatId:
    rows = boarding_pass[:7]
    columns = boarding_pass[7:]

    left_row = 0
    right_row = 127
    for character in rows:
        if character == "F":
            right_row = math.floor((left_row + right_row) / 2)
        else:
            left_row = math.ceil((left_row + right_row) / 2)

    left_column = 0
    right_column = 7
    for character in columns:
        if character == "L":
            right_column = math.floor((left_column + right_column) / 2)
        else:
            left_column = math.ceil((left_column + right_column) / 2)

    return left_row * 8 + left_column


def get_highest_seat_id(boarding_passes: list[BoardingPass]) -> SeatId:
    return max(get_seat_id(boarding_pass) for boarding_pass in boarding_passes)


def solution() -> None:
    """Solution to https://adventofcode.com/2020/day/5"""

    print(get_highest_seat_id(read_input()))


if __name__ == "__main__":
    solution()
