from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations, permutations
from typing import Callable


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


def create_antinode(
    a: tuple[int, int], b: tuple[int, int], r: int = 1
) -> tuple[int, int]:
    x1, y1 = a
    x2, y2 = b

    dx = x1 - x2
    dy = y1 - y2

    return (x1 + dx * r, y1 + dy * r)


def find_antinodes(
    locations: tuple[int, int], max_x: int, max_y: int
) -> set[tuple[int, int]]:
    antinodes = set()

    location_pairs = combinations(locations, 2)

    for pair in location_pairs:
        # checking antinodes above and bellow antennas
        for a, b in permutations(pair):
            antinode = create_antinode(a, b)
            if not is_out_of_bounds(max_x, max_y, antinode):
                antinodes.add(antinode)

    return antinodes


def find_antinodes_with_resonant_harmonics(
    locations: tuple[int, int], max_x: int, max_y: int
) -> set[tuple[int, int]]:
    antinodes = set()

    location_pairs = combinations(locations, 2)

    for pair in location_pairs:
        # antennas positions are also antinodes
        antinodes.add(pair[0])
        antinodes.add(pair[1])

        # checking antinodes above and bellow antennas
        for a, b in permutations(pair):
            iteration = 1

            antinode = create_antinode(a, b, iteration)
            while not is_out_of_bounds(max_x, max_y, antinode):
                antinodes.add(antinode)
                iteration += 1
                antinode = create_antinode(a, b, iteration)

    return antinodes


def count_unique_antinodes(antenna_map: AntennaMap, finder_function: Callable) -> int:
    unique_antinodes = set()

    for _, locations in antenna_map.locations_per_antenna.items():
        unique_antinodes.update(
            finder_function(locations, antenna_map.max_x, antenna_map.max_y)
        )

    return len(unique_antinodes)


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/8"""

    data = read_input("8.txt")
    print(count_unique_antinodes(data, finder_function=find_antinodes))
    print(
        count_unique_antinodes(
            data, finder_function=find_antinodes_with_resonant_harmonics
        )
    )


if __name__ == "__main__":
    solution()
