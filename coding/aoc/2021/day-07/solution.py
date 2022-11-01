from typing import List, Callable


def read_input() -> List[int]:
    with open("input.txt") as file:
        return [int(value) for value in file.readline().split(",")]


def calculate_lowest_fuel_costs(fuel_calculator: Callable, positions: List[int]) -> int:
    costs = {
        sum(fuel_calculator(position, possible_best_position) for position in positions)
        for possible_best_position in range(max(positions))
    }
    return min(costs)


def calculate_fuel(a: int, b: int) -> int:
    fuel = abs(a - b)
    return fuel


def get_min_required_fuel(positions: List[int]) -> int:
    return calculate_lowest_fuel_costs(calculate_fuel, positions)


def calculate_fuel_adjusted(a: int, b: int) -> int:
    steps = abs(a - b)
    fuel = round(steps * (steps + 1) / 2)
    return fuel


def get_min_required_fuel_adjusted(positions: List[int]) -> int:
    return calculate_lowest_fuel_costs(calculate_fuel_adjusted, positions)


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/7"""

    print(get_min_required_fuel(read_input()))
    print(get_min_required_fuel_adjusted(read_input()))


if __name__ == "__main__":
    solution()
