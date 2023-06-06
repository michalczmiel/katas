import math
from typing import NewType


BoardingPass = NewType("BoardingPass", str)
SeatRow = NewType("SeatRow", int)
SeatColumn = NewType("SeatColumn", int)
SeatId = NewType("SeatId", int)


def read_input() -> list[BoardingPass]:
    boarding_passes = []

    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            boarding_passes.append(line)

    return boarding_passes


def get_seat_row(boarding_pass: BoardingPass) -> SeatRow:
    rows = boarding_pass[:7]

    left_row = 0
    right_row = 127
    for character in rows:
        if character == "F":
            right_row = math.floor((left_row + right_row) / 2)
        else:
            left_row = math.ceil((left_row + right_row) / 2)

    return left_row


def get_seat_column(boarding_pass: BoardingPass) -> SeatColumn:
    columns = boarding_pass[-3:]

    left_column = 0
    right_column = 7
    for character in columns:
        if character == "L":
            right_column = math.floor((left_column + right_column) / 2)
        else:
            left_column = math.ceil((left_column + right_column) / 2)

    return left_column


def get_seat_id(boarding_pass: BoardingPass) -> SeatId:
    return get_seat_row(boarding_pass) * 8 + get_seat_column(boarding_pass)


def get_highest_seat_id(boarding_passes: list[BoardingPass]) -> SeatId:
    return max(get_seat_id(boarding_pass) for boarding_pass in boarding_passes)


def get_your_seat_id(boarding_passes: list[BoardingPass]) -> SeatId:
    seat_ids = sorted(get_seat_id(boarding_pass) for boarding_pass in boarding_passes)

    for index, seat_id in enumerate(seat_ids[1:]):
        expected_seat_id = seat_ids[index] + 1
        if seat_id != expected_seat_id:
            return expected_seat_id


def solution() -> None:
    """Solution to https://adventofcode.com/2020/day/5"""

    print(get_highest_seat_id(read_input()))
    print(get_your_seat_id(read_input()))


if __name__ == "__main__":
    solution()
