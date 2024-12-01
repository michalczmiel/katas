import re


def read_input(file_name: str) -> tuple[list[int], list[int]]:
    lists = ([], [])
    with open(file_name) as file:
        for line in file:
            location_ids = re.findall(r"\d+", line)

            for i, location_id in enumerate(location_ids):
                lists[i].append(int(location_id))

    return lists


def calculate_total_distance_between_lists(lists: tuple[list[int], list[int]]) -> int:
    first, second = lists

    first.sort()
    second.sort()

    total_distance = 0

    for a, b in zip(first, second):
        distance = abs(a - b)
        total_distance += distance

    return total_distance


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/1"""

    print(calculate_total_distance_between_lists(read_input("1.txt")))


if __name__ == "__main__":
    solution()
