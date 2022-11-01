import math
import itertools
from typing import List, NewType, Set, Tuple

HeightMap = NewType("HeightMap", List[List[int]])


def read_input() -> HeightMap:
    with open("input.txt") as file:
        heightmap = []
        for line in file.readlines():
            heightmap.append([int(height) for height in list(line.strip())])
        return heightmap


IGNORED_HEIGHT = 9


def calculate_low_points(heightmap: HeightMap) -> Set[Tuple[int, int]]:
    low_points = set()

    for x in range(len(heightmap)):
        for y in range(len(heightmap[x])):
            height = heightmap[x][y]
            if height == IGNORED_HEIGHT:
                continue

            left = heightmap[x][y - 1] if y - 1 >= 0 else None
            right = heightmap[x][y + 1] if y + 1 < len(heightmap[x]) else None
            down = heightmap[x + 1][y] if x + 1 < len(heightmap) else None
            up = heightmap[x - 1][y] if x - 1 >= 0 else None

            neighbors_height = [
                neighbor for neighbor in {left, right, up, down} if neighbor is not None
            ]

            if all(height < neighbor_height for neighbor_height in neighbors_height):
                low_points.add((x, y))

    return low_points


def calculate_risk_levels_sum(heightmap: HeightMap) -> int:
    low_points = calculate_low_points(heightmap)

    risk_levels = [heightmap[x][y] + 1 for x, y in low_points]

    return sum(risk_levels)


def basin_flood_fill(
    heightmap: HeightMap, x: int, y: int, checked: Set[Tuple[int, int]]
) -> None:
    if x < 0 or x >= len(heightmap) or y < 0 or y >= len(heightmap[0]):
        return

    if heightmap[x][y] == IGNORED_HEIGHT:
        return

    if (x, y) in checked:
        return

    checked.add((x, y))

    basin_flood_fill(heightmap, x, y - 1, checked)
    basin_flood_fill(heightmap, x, y + 1, checked)
    basin_flood_fill(heightmap, x - 1, y, checked)
    basin_flood_fill(heightmap, x + 1, y, checked)


def calculate_largest_basins_product(
    heightmap: HeightMap, basins_count: int = 3
) -> int:
    low_points = calculate_low_points(heightmap)
    basin_sizes = []

    for x, y in low_points:
        basin = set()
        basin_flood_fill(heightmap, x, y, basin)
        basin_sizes.append(len(basin))

    largest_basin_sizes = itertools.islice(
        sorted(basin_sizes, reverse=True), basins_count
    )
    return math.prod(largest_basin_sizes)


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/9"""

    print(calculate_risk_levels_sum(read_input()))
    print(calculate_largest_basins_product(read_input()))


if __name__ == "__main__":
    solution()
