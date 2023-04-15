import functools
import operator


def read_input() -> list[list[str]]:
    map = []
    with open("input.txt") as file:
        for line in file:
            map.append(list(line.strip()))
    return map


def count_trees(map: list[list[str]], right: int, down: int) -> int:
    tree_count = 0
    vertical_max = len(map) - 1
    horizontal = 0
    vertical = 0

    while vertical < vertical_max:
        horizontal += right

        horizontal_max = len(map[vertical])
        # check if out of pattern horizontally
        if horizontal >= horizontal_max:
            horizontal = horizontal - horizontal_max

        vertical += down

        if map[vertical][horizontal] == "#":
            tree_count += 1

    return tree_count


def count_trees_multiple_scopes(map: list[list[str]]) -> int:
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    tree_count_list = (count_trees(map, right, down) for right, down in slopes)

    return functools.reduce(operator.mul, tree_count_list)


def solution() -> None:
    """Solution to https://adventofcode.com/2020/day/3"""

    print(count_trees(read_input(), right=3, down=1))
    print(count_trees_multiple_scopes(read_input()))


if __name__ == "__main__":
    solution()
