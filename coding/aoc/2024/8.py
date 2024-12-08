from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations


@dataclass
class AntennaMap:
    max_y: int
    max_x: int
    locations_per_antenna: dict[str, tuple[int, int]]


def read_input(file_name: str) -> AntennaMap:
    locations = defaultdict(set)

    max_y = 0
    max_x = 0

    for y, line in enumerate(open(file_name)):
        max_y = max(max_y, y)
        for x, char in enumerate(line.strip()):
            max_x = max(max_x, x)
            if char != ".":
                locations[char].add((x, y))

    return AntennaMap(max_y, max_x, locations)


def is_out_of_bounds(max_x: int, max_y: int, point: tuple[int, int]) -> bool:
    x, y = point

    return x > max_x or y > max_y or x < 0 or y < 0


def find_antinodes(
    locations: tuple[int, int], max_x: int, max_y: int
) -> set[tuple[int, int]]:
    antinodes = set()

    location_pairs = combinations(locations, 2)

    for (x1, y1), (x2, y2) in location_pairs:
        v1 = (x1 - x2, y1 - y2)
        a1 = (x1 + v1[0], y1 + v1[1])

        if not is_out_of_bounds(max_x, max_y, a1):
            antinodes.add(a1)

        v2 = (x2 - x1, y2 - y1)
        a2 = (x2 + v2[0], y2 + v2[1])

        if not is_out_of_bounds(max_x, max_y, a2):
            antinodes.add(a2)

    return antinodes


def count_unique_antinodes(antenna_map: AntennaMap) -> int:
    unique_antinodes = set()

    for _, locations in antenna_map.locations_per_antenna.items():
        unique_antinodes.update(
            find_antinodes(locations, antenna_map.max_x, antenna_map.max_y)
        )

    return len(unique_antinodes)


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/8"""

    data = read_input("8.txt")
    print(count_unique_antinodes(data))


if __name__ == "__main__":
    solution()
