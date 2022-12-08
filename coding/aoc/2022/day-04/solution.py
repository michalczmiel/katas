from typing import NewType

Pair = NewType("Pair", tuple[list[int]])


def read_input(file_name: str) -> list[Pair]:
    pairs = []

    with open(file_name) as file:
        for line in file:
            first, second = line.strip().split(",")
            first = [int(number) for number in first.split("-")]
            second = [int(number) for number in second.split("-")]

            pairs.append((first, second))
    return pairs


def count_pairs_fully_contain(pairs: list[Pair]) -> int:
    count = 0

    for first, second in pairs:
        first_min, first_max = first
        second_min, second_max = second

        if (first_min >= second_min and first_max <= second_max) or (
            second_min >= first_min and second_max <= first_max
        ):
            count += 1

    return count


def count_pairs_overlap(pairs: list[Pair]) -> int:
    count = 0

    for first, second in pairs:
        first_min, first_max = first
        second_min, second_max = second

        if (first_min >= second_min and first_min <= second_max) or (
            second_min >= first_min and second_min <= first_max
        ):
            count += 1

    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2022/day/4"""

    print(count_pairs_fully_contain(read_input("input.txt")))
    print(count_pairs_overlap(read_input("input.txt")))


if __name__ == "__main__":
    solution()
