from collections import defaultdict


def read_input(file_name: str) -> list[str]:
    lines = []

    with open(file_name, "r") as file:
        for line in file:
            lines.append(line.strip())

    return lines


SYMBOLS = {"*", "#", "+", "-", "$", "/", "=", "@", "%", "&"}
POSSIBLE_GEAR_SYMBOL = "*"

def get_neighboring_points(x: int, y: int) -> set[tuple[int, int]]:
    return {
        (x + 1, y),
        (x - 1, y),
        (x + 1, y + 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y - 1),
        (x, y + 1),
        (x, y - 1),
    }


def get_part_numbers(lines: list[str]) -> int:
    temp_number = ""
    coordinates = set()
    numbers_with_coordinates = defaultdict(list)
    symbol_coordinates = set()

    for i, line in enumerate(lines):
        for j, element in enumerate(line):
            point = (i, j)

            if element in SYMBOLS:
                symbol_coordinates.add(point)

            if element.isdigit():
                coordinates.add(point)
                temp_number += str(element)

            if (not element.isdigit() or j == len(line) - 1) and temp_number:
                numbers_with_coordinates[temp_number].append(coordinates.copy())
                temp_number = ""
                coordinates.clear()

    part_numbers = []
    for number, number_coordinates_list in numbers_with_coordinates.items():
        for number_coordinates in number_coordinates_list:
            for coordinate in symbol_coordinates:
                x, y = coordinate

                nearby_points = get_neighboring_points(x, y)

                if nearby_points.intersection(number_coordinates):
                    part_numbers.append(int(number))

    return sum(part_numbers)


def get_gear_ration(lines: list[str]) -> int:
    temp_number = ""
    coordinates = set()
    numbers_with_coordinates = defaultdict(list)
    part_coordinates = set()

    for i, line in enumerate(lines):
        for j, element in enumerate(line):
            point = (i, j)

            if element == POSSIBLE_GEAR_SYMBOL:
                part_coordinates.add(point)

            if element.isdigit():
                coordinates.add(point)
                temp_number += str(element)

            if (not element.isdigit() or j == len(line) - 1) and temp_number:
                numbers_with_coordinates[temp_number].append(coordinates.copy())
                temp_number = ""
                coordinates.clear()

    gear_ratios = []
    for gear_coordinate in part_coordinates:
        x, y = gear_coordinate

        nearby_points = get_neighboring_points(x, y)

        part_numbers = []
        for number, number_coordinates_list in numbers_with_coordinates.items():
            for number_coordinates in number_coordinates_list:
                if nearby_points.intersection(number_coordinates):
                    part_numbers.append(number)

        if len(part_numbers) == 2:
            gear_ratios.append(int(part_numbers[0]) * int(part_numbers[1]))

    return sum(gear_ratios)


def solution() -> None:
    """Solution to https://adventofcode.com/2023/day/3"""

    print(get_part_numbers(read_input("input.txt")))
    print(get_gear_ration(read_input("input.txt")))


if __name__ == "__main__":
    solution()
