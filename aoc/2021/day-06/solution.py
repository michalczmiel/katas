from typing import List


def read_input() -> List[int]:
    with open("input.txt") as file:
        return [int(value) for value in file.readline().split(",")]


def count_lanternfish_after_80_days(initialLanternfishes: List[int]) -> int:
    days = 80

    lanternfish_pool = initialLanternfishes.copy()

    for day in range(days):
        new_pool = []

        for lanterfish_timer in lanternfish_pool:
            if lanterfish_timer == 0:
                new_pool.append(6)
                new_pool.append(8)
            else:
                new_pool.append(lanterfish_timer - 1)
        lanternfish_pool = new_pool

    return len(lanternfish_pool)


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/6"""

    print(count_lanternfish_after_80_days(read_input()))


if __name__ == "__main__":
    solution()
