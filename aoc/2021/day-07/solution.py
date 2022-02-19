from typing import List


def read_input() -> List[int]:
    with open("input.txt") as file:
        return [int(value) for value in file.readline().split(",")]


def count_required_fuel(positions: List[int]) -> int:
    costs = {
        sum(abs(position - possible_best_position) for position in positions)
        for possible_best_position in range(max(positions))
    }

    return min(costs)


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/7"""

    print(count_required_fuel(read_input()))


if __name__ == "__main__":
    solution()
