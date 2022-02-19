from typing import List
from collections import Counter


def read_input() -> List[int]:
    with open("input.txt") as file:
        return [int(value) for value in file.readline().split(",")]


def count_lanternfish(
    timers: List[int], days: int, starting_timer: int = 8, producing_timer: int = 6
):
    state = Counter(timers)

    for day in range(days):
        new_state = {}
        new_fishes = state[0]

        for timer in range(starting_timer):
            new_state[timer] = state[timer + 1]

            if timer == producing_timer:
                new_state[timer] += new_fishes

        new_state[starting_timer] = new_fishes
        state = new_state

    count = sum(state.values())
    return count


def count_lanternfish_after_80_days(timers: List[int]) -> int:
    return count_lanternfish(timers, days=80)


def count_lanternfish_after_256_days(timers: List[int]) -> int:
    return count_lanternfish(timers, days=256)


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/6"""

    print(count_lanternfish_after_80_days(read_input()))
    print(count_lanternfish_after_256_days(read_input()))


if __name__ == "__main__":
    solution()
