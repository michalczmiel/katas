from typing import List, Tuple
from collections import Counter


def read_input() -> List[Tuple[int, int, int, int]]:
    lines = []

    with open("input.txt") as file:
        for line in file.readlines():
            start, end = line.strip().split(" -> ")

            x1, y1 = [int(x) for x in start.split(",")]
            x2, y2 = [int(x) for x in end.split(",")]

            lines.append((x1, y1, x2, y2))
    return lines


def count_overlap_points_horizontal_and_vertical(
    lines: List[Tuple[int, int, int, int]]
):
    overlaps_counter = Counter()

    for x1, y1, x2, y2 in lines:
        if x1 == x2:
            y_min = min(y1, y2)
            y_max = max(y1, y2)

            overlaps_counter.update((x1, y) for y in range(y_min, y_max + 1))

        elif y1 == y2:
            x_min = min(x1, x2)
            x_max = max(x1, x2)

            overlaps_counter.update((x, y1) for x in range(x_min, x_max + 1))

    count = len(
        [
            overlap_count
            for overlap_count in overlaps_counter.values()
            if overlap_count >= 2
        ]
    )
    return count


def count_overlap_points_horizontal_vertical_diagonal(
    lines: List[Tuple[int, int, int, int]]
):
    overlaps_counter = Counter()

    for x1, y1, x2, y2 in lines:
        if x1 == x2:
            y_min = min(y1, y2)
            y_max = max(y1, y2)

            overlaps_counter.update((x1, y) for y in range(y_min, y_max + 1))

        elif y1 == y2:
            x_min = min(x1, x2)
            x_max = max(x1, x2)

            overlaps_counter.update((x, y1) for x in range(x_min, x_max + 1))

        if abs(x1 - x2) == abs(y1 - y2):
            x_delta = 1 if x1 < x2 else -1
            y_delta = 1 if y1 < y2 else -1

            points = []

            current_x1 = x1
            current_y1 = y1

            points.append((current_x1, current_y1))
            while current_x1 != x2 and current_y1 != y2:
                current_x1 += x_delta
                current_y1 += y_delta
                points.append((current_x1, current_y1))

            overlaps_counter.update(points)

    count = len(
        [
            overlap_count
            for overlap_count in overlaps_counter.values()
            if overlap_count >= 2
        ]
    )
    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/5"""

    print(count_overlap_points_horizontal_and_vertical(read_input()))
    print(count_overlap_points_horizontal_vertical_diagonal(read_input()))


if __name__ == "__main__":
    solution()
