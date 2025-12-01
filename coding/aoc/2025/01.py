from typing import NewType

LEFT = "L"
RIGHT = "R"

DIAL_MAX = 100
DIAL_MIN = 0

Rotation = NewType("Rotation", tuple[str, int])


def read_input(file_name: str) -> list[Rotation]:
    lines = []
    with open(file_name) as file:
        for line in file:
            direction, *rotation = list(line.strip())
            rotation = "".join(rotation)

            lines.append((direction, int(rotation)))
    return lines


def rotate_dial(current_position: int, direction: str, distance: int) -> int:
    """
    Rotates the dial left or right and returns new position

    >>> rotate_dial(11, "R", 8)
    19
    >>> rotate_dial(19, "L", 19)
    0
    >>> rotate_dial(0, "L", 1)
    99
    >>> rotate_dial(0, "R", 100)
    0
    >>> rotate_dial(0, "L", 100)
    0
    """

    new_position = (
        current_position + distance
        if direction == RIGHT
        else current_position - distance
    )

    return new_position % DIAL_MAX


def count_dial_point(
    current_position: int, direction: str, distance: int, target_dial=0
) -> tuple[int, int]:
    """
    Checks if during rotation the dial pointed at 0

    >>> count_dial_point(50, "L", 68)
    (1, 82)
    >>> count_dial_point(95, "R", 55)
    (1, 50)
    >>> count_dial_point(50, "R", 1000)
    (10, 50)

    """

    count = 0

    new_position = current_position

    for i in range(distance):
        if direction == LEFT:
            new_position -= 1
        else:
            new_position += 1

        new_position = new_position % DIAL_MAX

        if new_position == target_dial:
            count += 1

    return count, new_position


def count_dials_pointing_at(
    rotations: list[Rotation], dial: int, current_position=50
) -> int:
    zero_count = 0

    for direction, distance in rotations:
        new_position = rotate_dial(current_position, direction, distance)

        if new_position == 0:
            zero_count += 1
        current_position = new_position

    return zero_count


def second_count_dials_pointing_at(
    rotations: list[Rotation], dial: int, current_position=50
) -> int:
    zero_count = 0

    for direction, distance in rotations:
        count, new_position = count_dial_point(current_position, direction, distance)

        zero_count += count

        current_position = new_position

    return zero_count


def solution() -> None:
    """Solution to https://adventofcode.com/2025/day/1"""

    rotations = read_input("01.txt")

    print(count_dials_pointing_at(rotations, dial=0))
    print(second_count_dials_pointing_at(rotations, dial=0))


if __name__ == "__main__":
    solution()
