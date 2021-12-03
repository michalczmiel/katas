from collections import deque
from typing import Iterator


def read_input() -> Iterator[int]:
    with open("input.txt") as file:
        for line in file.readlines():
            yield int(line)


def get_measurements_increase_count(measurements: Iterator[int]) -> int:
    previous_measurement = None
    count = 0

    for measurement in measurements:
        if previous_measurement and measurement > previous_measurement:
            count += 1

        previous_measurement = measurement

    return count


def get_measurements_sliding_window_sum_increase_count(
    measurements: Iterator[int],
) -> int:
    previous_sliding_window_sum = None
    sliding_window = deque()
    count = 0

    for measurement in measurements:
        sliding_window.append(measurement)

        if len(sliding_window) == 3:
            sliding_window_sum = sum(sliding_window)

            if (
                previous_sliding_window_sum
                and sliding_window_sum > previous_sliding_window_sum
            ):
                count += 1

            previous_sliding_window_sum = sliding_window_sum
            sliding_window.popleft()

    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/1"""

    print(get_measurements_increase_count(read_input()))
    print(get_measurements_sliding_window_sum_increase_count(read_input()))


if __name__ == "__main__":
    solution()
