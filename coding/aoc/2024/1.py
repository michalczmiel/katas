from collections import Counter
from typing import NewType

LocationLists = NewType("LocationLists", tuple[list[int], list[int]])


def read_input(file_name: str) -> LocationLists:
    with open(file_name) as file:
        lines = file.readlines()

    lists = ([], [])
    for line in lines:
        location_ids = line.split()

        for i, location_id in enumerate(location_ids):
            lists[i].append(int(location_id))

    return lists


def calculate_total_distance_between_lists(lists: LocationLists) -> int:
    first, second = lists

    assert len(first) == len(second)

    first.sort()
    second.sort()

    total_distance = sum(abs(a - b) for a, b in zip(first, second))

    return total_distance


def calculate_total_similarity_score(lists: LocationLists) -> int:
    first, second = lists

    counter = Counter(second)

    total_similarity_score = sum(
        number * counter[number] for number in first if number in counter
    )

    return total_similarity_score


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/1"""

    data = read_input("1.txt")

    print(calculate_total_distance_between_lists(data))
    print(calculate_total_similarity_score(data))


if __name__ == "__main__":
    solution()
