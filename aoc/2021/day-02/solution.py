from dataclasses import dataclass
from enum import Enum
from typing import Iterator, Tuple


class Direction(Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"


@dataclass
class Submarine:
    horizontal_position: int = 0
    depth: int = 0

    def move(self, direction: str, value: int) -> None:
        if direction == Direction.FORWARD.value:
            self.horizontal_position += value
        elif direction == Direction.DOWN.value:
            self.depth += value
        elif direction == Direction.UP.value:
            self.depth -= value


def read_input() -> Iterator[Tuple[str, int]]:
    with open("input.txt") as file:
        for line in file.readlines():
            direction, value = line.split()
            yield direction, int(value)


def get_product_of_horizontal_position_and_depth(
    commands: Iterator[Tuple[str, int]]
) -> int:
    submarine = Submarine()

    for direction, value in commands:
        submarine.move(direction, value)

    return submarine.horizontal_position * submarine.depth


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/2"""
    print(get_product_of_horizontal_position_and_depth(read_input()))


if __name__ == "__main__":
    solution()
