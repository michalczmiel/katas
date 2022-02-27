from typing import List, NewType

HeightMap = NewType("HeightMap", List[List[int]])


def read_input() -> HeightMap:
    with open("input.txt") as file:
        heightmap = []
        for line in file.readlines():
            heightmap.append([int(height) for height in list(line.strip())])
        return heightmap


def calculate_risk_levels_sum(heightmap: HeightMap) -> int:
    risk_levels = []

    for x in range(len(heightmap)):
        for y in range(len(heightmap[x])):
            current = heightmap[x][y]
            left = heightmap[x][y - 1] if y - 1 >= 0 else None
            right = heightmap[x][y + 1] if y + 1 < len(heightmap[x]) else None
            up = heightmap[x + 1][y] if x + 1 < len(heightmap) else None
            down = heightmap[x - 1][y] if x - 1 >= 0 else None

            neighbors = [
                neighbor for neighbor in {left, right, up, down} if neighbor is not None
            ]

            if all(current < neighbor for neighbor in neighbors):
                risk_levels.append(current + 1)

    return sum(risk_levels)


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/9"""

    print(calculate_risk_levels_sum(read_input()))


if __name__ == "__main__":
    solution()
