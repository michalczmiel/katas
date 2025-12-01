LEFT = "L"
RIGHT = "R"


def read_input(file_name: str) -> list[tuple[str, int]]:
    lines = []
    with open(file_name) as file:
        for line in file:
            direction, *rotation = list(line.strip())
            rotation = "".join(rotation)

            lines.append((direction, rotation))
    return lines


def rotate_dial(current_position: int, direction: str, value: int) -> int:
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

    return -1


def count_dials_pointing_at(passwords: list[str], dial: int) -> int:
    return 0


def solution() -> None:
    """Solution to https://adventofcode.com/2025/day/1"""

    print(count_dials_pointing_at(read_input("01-small.txt"), dial=0))


if __name__ == "__main__":
    solution()
