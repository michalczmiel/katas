from typing import Iterable, NewType


Mass = NewType("Mass", int)
Fuel = NewType("Fuel", int)


def read_input() -> Iterable[Mass]:
    with open("input.txt") as file:
        for line in file:
            yield int(line)


def calculate_required_fuel(mass: Mass) -> Fuel:
    return mass // 3 - 2


def calculate_sum_of_fuel_requirements(modules_mass: Iterable[Mass]) -> Fuel:
    total_fuel = 0

    for mass in modules_mass:
        total_fuel += calculate_required_fuel(mass)

    return total_fuel


def calculate_sum_of_fuel_requirements_adjusted(modules_mass: Iterable[Mass]) -> Fuel:
    total_fuel = 0

    for mass in modules_mass:
        initial_fuel = calculate_required_fuel(mass)

        total_fuel += initial_fuel

        additional_fuel = calculate_required_fuel(initial_fuel)
        while additional_fuel > 0:
            total_fuel += additional_fuel

            additional_fuel = calculate_required_fuel(additional_fuel)

    return total_fuel


def solution() -> None:
    """Solution to https://adventofcode.com/2019/day/1"""

    print(calculate_sum_of_fuel_requirements(read_input()))
    print(calculate_sum_of_fuel_requirements_adjusted(read_input()))


if __name__ == "__main__":
    solution()
