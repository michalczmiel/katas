def read_input(file_name: str) -> list[str]:
    rucksacks = []

    with open(file_name) as file:
        for line in file:
            rucksacks.append(line.strip())
    return rucksacks


def get_common_item_in_rucksack(rucksack: str) -> str:
    first_compartment_unique_items = set()
    compartment_size = len(rucksack) // 2
    for index, item in enumerate(rucksack):
        is_first_compartment = index < compartment_size

        if is_first_compartment and item not in first_compartment_unique_items:
            first_compartment_unique_items.add(item)
            continue

        if not is_first_compartment and item in first_compartment_unique_items:
            return item


def get_item_priority(item: str) -> int:
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38


def get_item_priorities_sum(rucksacks: list[str]):
    priorities_sum = 0
    for rucksack in rucksacks:
        common_item = get_common_item_in_rucksack(rucksack)
        priority = get_item_priority(common_item)
        priorities_sum += priority

    return priorities_sum


def get_item_types_priorities_sum(rucksacks: list[str], group_size: int = 3):
    priorities_sum = 0

    for g in range(0, len(rucksacks), group_size):
        # compute unique items in each rucksack for a given group
        unique_items_in_group = {r: set(rucksacks[g + r]) for r in range(0, group_size)}
        unique_items = set.intersection(*unique_items_in_group.values())
        # we assume there is only one unique item type across the group
        item = unique_items.pop()
        priorities_sum += get_item_priority(item)

    return priorities_sum


def solution() -> None:
    """Solution to https://adventofcode.com/2022/day/3"""

    print(get_item_priorities_sum(read_input("input.txt")))
    print(get_item_types_priorities_sum(read_input("input.txt")))


if __name__ == "__main__":
    solution()
