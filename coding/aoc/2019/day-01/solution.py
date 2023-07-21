from typing import Iterable, NewType


Mass = NewType("Mass", int)


def read_input() -> Iterable[Mass]:
    with open("input.txt") as file:
        for line in file:
            yield int(line)


def calculate_sum_of_fuel_requirements(modules_mass: Iterable[Mass]) -> int:
    fuel_requirement_sum = 0

    for mass in modules_mass:
        fuel_requirement = mass // 3 - 2

        fuel_requirement_sum += fuel_requirement

    return fuel_requirement_sum


def solution() -> None:
    """Solution to https://adventofcode.com/2019/day/1"""

    print(calculate_sum_of_fuel_requirements(read_input()))


if __name__ == "__main__":
    solution()
