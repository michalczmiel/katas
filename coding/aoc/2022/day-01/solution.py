from typing import Iterator


def read_input(file_name: str) -> Iterator[list[int]]:
    inventories = []
    inventory = []
    with open(file_name) as file:
        for line in file:
            if line == "\n":
                yield inventory
                inventory = []
            else:
                inventory.append(int(line.strip()))


def get_top_carried_calories(inventories: Iterator[list[int]], max_count: int = 3) -> int:
    max_calories = []
    to_insert = None

    for inventory in inventories:
        calories_sum = sum(inventory)

        # skip if sum is smaller than current minimum
        if max_calories and calories_sum < max_calories[0]:
            continue

        for index, item in enumerate(max_calories):
            if calories_sum >= item:
                continue
            else:
                # index for new sum between existing sums
                to_insert = index - 1
                break

        if to_insert is not None:
            max_calories.insert(to_insert, calories_sum)
            to_insert = None
        else:
            max_calories.append(calories_sum)

        # remove lowest value if reached max count
        if len(max_calories) > max_count:
            max_calories.pop(0)

    return sum(max_calories)


def get_most_carried_calories(inventories: Iterator[list[int]]) -> int:
    max_calories = 0

    for inventory in inventories:
        calories_sum = sum(inventory)

        if calories_sum > max_calories:
            max_calories = calories_sum

    return max_calories


def solution() -> None:
    """Solution to https://adventofcode.com/2022/day/1"""

    print(get_most_carried_calories(read_input("input.txt")))
    print(get_top_carried_calories(read_input("input.txt")))


if __name__ == "__main__":
    solution()
