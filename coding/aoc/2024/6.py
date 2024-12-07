from typing import NewType

EMPTY = 0
OBSTRUCTION = 1
GUARD = 2

LabMap = NewType("LabMap", dict[tuple[int, int], int])


def read_input(file_name: str) -> LabMap:
    lab_map = {}
    element_mapping = {
        ".": EMPTY,
        "#": OBSTRUCTION,
        "^": GUARD,
    }

    for y, line in enumerate(open(file_name)):
        for x, char in enumerate(line.strip()):
            lab_map[(x, y)] = element_mapping[char]

    return lab_map


def find_start_position(lab_map: LabMap) -> tuple[int, int]:
    for (x, y), element in lab_map.items():
        if element == GUARD:
            return (x, y)


def get_next_position(
    current: tuple[int, int], direction: tuple[int, int]
) -> tuple[int, int]:
    return (
        current[0] + direction[0],
        current[1] + direction[1],
    )


def rotate_direction(direction: tuple[int, int]) -> tuple[int, int]:
    direction_rotation_mapping = {
        (0, -1): (1, 0),
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
    }

    return direction_rotation_mapping[direction]


def walk(lab_map: LabMap) -> list:
    path = []
    direction = (0, -1)
    current = find_start_position(lab_map)

    while True:
        path.append(current)

        next_position = get_next_position(current, direction)

        next_element = lab_map.get(next_position)
        if next_element is None:
            return path

        while next_element == OBSTRUCTION:
            direction = rotate_direction(direction)
            next_position = get_next_position(current, direction)
            next_element = lab_map.get(next_position)

        current = next_position


def check_if_loop(lab_map: LabMap, start: tuple[int, int]) -> bool:
    direction = (0, -1)
    current = start
    visited = set()

    while True:
        if current is None:
            return False

        x, y = current
        if (x, y, direction) in visited:
            return True

        visited.add((x, y, direction))

        next_position = get_next_position(current, direction)

        next_element = lab_map.get(next_position)
        if next_element is None:
            return False

        while next_element == OBSTRUCTION:
            direction = rotate_direction(direction)
            next_position = get_next_position(current, direction)
            next_element = lab_map.get(next_position)

        current = next_position


def count_visited_positions(lab_map: LabMap) -> int:
    path = walk(lab_map)

    return len(set(path))


def count_possible_obstructions(lab_map: LabMap) -> int:
    path = walk(lab_map)
    unique_path = list(dict.fromkeys(path))

    count = 0
    start = unique_path[0]

    for position in unique_path:
        original_value = lab_map[position]

        lab_map[position] = OBSTRUCTION

        if check_if_loop(lab_map, start):
            count += 1

        lab_map[position] = original_value

    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/6"""

    lab_map = read_input("6.txt")
    print(count_visited_positions(lab_map))
    print(count_possible_obstructions(lab_map))


if __name__ == "__main__":
    solution()
