from collections import defaultdict, Counter
from typing import Iterator


def read_input() -> Iterator[str]:
    with open("input.txt") as file:
        for line in file.readlines():
            yield line


def calculate_power_consumption(diagnostic: Iterator[str]) -> int:
    counts = defaultdict(lambda: {"0": 0, "1": 0})

    for number in diagnostic:
        for index in range(12):
            counts[index][number[index]] += 1

    gamma_rate_binary = ""
    epsilon_rate_binary = ""

    for count in counts.values():
        if count["1"] > count["0"]:
            gamma_rate_binary += "1"
            epsilon_rate_binary += "0"
        else:
            gamma_rate_binary += "0"
            epsilon_rate_binary += "1"

    gamma_rate = int(gamma_rate_binary, 2)
    epsilon_rate = int(epsilon_rate_binary, 2)

    return gamma_rate * epsilon_rate


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/3"""

    print(calculate_power_consumption(read_input()))


if __name__ == "__main__":
    solution()
