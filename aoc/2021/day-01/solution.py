from typing import Iterable


def read_input() -> Iterable[int]:
    with open("input.txt") as file:
        return [int(line) for line in file.readlines()]


def get_measurements_increase_count(measurements: Iterable[int]) -> int:
    previous_measurement = None
    count = 0

    for measurement in measurements:
        if previous_measurement and measurement > previous_measurement:
            count += 1

        previous_measurement = measurement

    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/1"""

    measurements = read_input()

    print(get_measurements_increase_count(measurements))


if __name__ == "__main__":
    solution()
