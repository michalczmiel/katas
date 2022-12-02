from typing import List


def read_input(file_name: str) -> List:
    inventories = []
    inventory = []
    with open(file_name) as file:
        for line in file:
            if line == "\n":
                inventories.append(inventory)
                inventory = []
                continue
            else:
                inventory.append(int(line.strip()))

    if inventory:
        inventories.append(inventory)

    return inventories


def get_most_carried_calories(inventories: List[List[int]]) -> int:
    max_calories = 0

    for inventory in inventories:
        calories_sum = sum(inventory)

        if calories_sum > max_calories:
            max_calories = calories_sum

    return max_calories


def solution() -> None:
    """Solution to https://adventofcode.com/2022/day/2"""

    print(get_most_carried_calories(read_input("input.txt")))


if __name__ == "__main__":
    solution()
