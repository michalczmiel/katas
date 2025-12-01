LEFT = "L"
RIGHT = "R"

DIAL_MAX = 100
DIAL_MIN = 0


def read_input(file_name: str) -> list[tuple[str, int]]:
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

    # handle values that "loop" around the dial
    target_dial = distance % DIAL_MAX

    if direction == RIGHT:
        return (current_position + target_dial) % DIAL_MAX

    new_position = current_position - target_dial
    if new_position < 0:
        return DIAL_MAX + new_position

    return new_position


def count_dials_pointing_at(
    passwords: list[tuple], dial: int, current_position=50
) -> int:
    zero_count = 0

    for direction, distance in passwords:
        new_position = rotate_dial(current_position, direction, distance)

        if new_position == 0:
            zero_count += 1
        current_position = new_position

    return zero_count


def solution() -> None:
    """Solution to https://adventofcode.com/2025/day/1"""

    print(count_dials_pointing_at(read_input("01.txt"), dial=0))


if __name__ == "__main__":
    solution()
