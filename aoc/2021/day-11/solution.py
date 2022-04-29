import copy
from typing import List, Tuple


EnergyLevels = List[List[int]]


def read_input() -> EnergyLevels:
    with open("input.txt") as file:
        energy_levels = []

        for line in file.readlines():
            energy_levels.append([int(energy_level) for energy_level in line.strip()])

        return energy_levels


def flash(energy_levels: EnergyLevels, flashed: set, x: int, y: int) -> None:
    if (x, y) in flashed:
        return

    if x < 0 or x >= len(energy_levels) or y < 0 or y >= len(energy_levels[0]):
        return

    if energy_levels[x][y] == 10:
        flashed.add((x, y))
        energy_levels[x][y] = 0

        flash(energy_levels, flashed, x, y - 1)
        flash(energy_levels, flashed, x, y + 1)
        flash(energy_levels, flashed, x - 1, y)
        flash(energy_levels, flashed, x + 1, y)

        # diagonally
        flash(energy_levels, flashed, x + 1, y + 1)
        flash(energy_levels, flashed, x - 1, y - 1)
        flash(energy_levels, flashed, x + 1, y - 1)
        flash(energy_levels, flashed, x - 1, y + 1)

    else:
        energy_levels[x][y] += 1

        if energy_levels[x][y] == 10:
            flash(energy_levels, flashed, x, y)


def update_energy_levels(energy_levels: EnergyLevels) -> Tuple[EnergyLevels, int]:
    updated_energy_levels = copy.deepcopy(energy_levels)

    points_to_flash = set()
    for x in range(len(energy_levels)):
        for y in range(len(energy_levels[x])):
            updated_energy_levels[x][y] = energy_levels[x][y] + 1
            if updated_energy_levels[x][y] == 10:
                points_to_flash.add((x, y))

    flashed = set()
    for x, y in points_to_flash:
        flash(updated_energy_levels, flashed, x, y)

    return updated_energy_levels, len(flashed)


def count_flashes_after_100_steps(energy_levels: EnergyLevels) -> int:
    total_flashed_count = 0

    for _ in range(100):
        energy_levels, flashed_count = update_energy_levels(energy_levels)
        total_flashed_count += flashed_count

    return total_flashed_count


def get_first_flash_step(energy_levels: EnergyLevels) -> int:
    found_step = None
    current_step = 1

    while not found_step:
        energy_levels, flashed_count = update_energy_levels(energy_levels)

        if flashed_count == 100:
            found_step = current_step
        current_step += 1

    return found_step


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/11"""

    print(count_flashes_after_100_steps(read_input()))
    print(get_first_flash_step(read_input()))


if __name__ == "__main__":
    solution()
