from typing import List, Tuple, NewType
from collections import Counter
from dataclasses import dataclass


Point = NewType("Point", Tuple[int, int])


@dataclass(frozen=True)
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def is_horizontal(self) -> bool:
        return self.x1 == self.x2

    @property
    def is_vertical(self) -> bool:
        return self.y1 == self.y2

    @property
    def is_45_deg_diagonal(self) -> bool:
        return abs(self.x1 - self.x2) == abs(self.y1 - self.y2)


def get_horizontal_points(line: Line) -> List[Point]:
    y_min = min(line.y1, line.y2)
    y_max = max(line.y1, line.y2)

    return [(line.x1, y) for y in range(y_min, y_max + 1)]


def get_vertical_points(line: Line) -> List[Point]:
    x_min = min(line.x1, line.x2)
    x_max = max(line.x1, line.x2)

    return [(x, line.y1) for x in range(x_min, x_max + 1)]


def get_45_diagonal_points(line: Line) -> List[Point]:
    x_delta = 1 if line.x1 < line.x2 else -1
    y_delta = 1 if line.y1 < line.y2 else -1

    current_x1 = line.x1
    current_y1 = line.y1

    points = [(current_x1, current_y1)]
    while current_x1 != line.x2 and current_y1 != line.y2:
        current_x1 += x_delta
        current_y1 += y_delta
        points.append((current_x1, current_y1))
    return points


def read_input() -> List[Line]:
    lines = []

    with open("input.txt") as file:
        for line in file.readlines():
            start, end = line.strip().split(" -> ")

            x1, y1 = [int(value) for value in start.split(",")]
            x2, y2 = [int(value) for value in end.split(",")]

            lines.append(Line(x1, y1, x2, y2))
    return lines


def count_overlap_points_horizontal_and_vertical(lines: List[Line]):
    overlaps_counter = Counter()

    for line in lines:
        points = []

        if line.is_horizontal:
            points = get_horizontal_points(line)
        elif line.is_vertical:
            points = get_vertical_points(line)

        if points:
            overlaps_counter.update(points)

    count = len(
        [
            overlap_count
            for overlap_count in overlaps_counter.values()
            if overlap_count >= 2
        ]
    )
    return count


def count_overlap_points_horizontal_vertical_diagonal(lines: List[Line]):
    overlaps_counter = Counter()

    for line in lines:
        points = []

        if line.is_horizontal:
            points = get_horizontal_points(line)
        elif line.is_vertical:
            points = get_vertical_points(line)
        elif line.is_45_deg_diagonal:
            points = get_45_diagonal_points(line)

        if points:
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
