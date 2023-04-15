def read_input() -> list[list[str]]:
    map = []
    with open("input.txt") as file:
        for line in file:
            map.append(list(line.strip()))
    return map


def count_trees(map: list[list[str]]) -> int:
    tree_count = 0
    vertical_max = len(map) - 1
    horizontal = 0
    vertical = 0

    while vertical < vertical_max:
        horizontal += 3

        horizontal_max = len(map[vertical])
        # check if out of pattern horizontally
        if horizontal >= horizontal_max:
            horizontal = horizontal - horizontal_max

        vertical += 1

        if map[vertical][horizontal] == "#":
            tree_count += 1

    return tree_count


def solution() -> None:
    """Solution to https://adventofcode.com/2020/day/3"""

    print(count_trees(read_input()))


if __name__ == "__main__":
    solution()
