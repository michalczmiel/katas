from collections import defaultdict
from typing import NewType

Rules = NewType("Rules", list[tuple[int, int]])
Update = NewType("Update", list[int])


def read_input(file_name: str) -> tuple[Rules, list[Update]]:
    rules = []
    updates = []

    for line in open(file_name):
        if line == "\n":
            continue

        if "|" in line:
            rules.append([int(rule) for rule in line.strip().split("|")])
        else:
            updates.append([int(page) for page in line.strip().split(",")])

    return rules, updates


def is_correct_update(page_ordering: dict[int, set], update: Update) -> bool:
    for i in range(1, len(update)):
        number = update[i]
        numbers_after = page_ordering.get(number, set())

        for j in range(0, i):
            previous_number = update[j]

            if previous_number in numbers_after:
                return False
    return True


def sum_middle_page_from_correct_updates(rules: Rules, updates: list[Update]) -> int:
    page_ordering = defaultdict(set)
    for first, second in rules:
        page_ordering[first].add(second)

    total_sum = 0

    for update in updates:
        if is_correct_update(page_ordering, update):
            total_sum += update[len(update) // 2]

    return total_sum


def sort_update(page_ordering: dict[int, set], update: Update) -> Update:
    """
    Current time complexity is O(n^2), could be improved
    """
    ordered = update.copy()

    for i in range(1, len(ordered)):
        current = ordered[i]
        numbers_after = page_ordering.get(current, set())

        for j in range(0, i):
            previous = ordered[j]

            if previous in numbers_after:
                ordered.insert(j, current)
                del ordered[i + 1]
                break

    return ordered


def sum_middle_page_from_incorrect_updates(rules: Rules, updates: list[Update]) -> int:
    page_ordering = defaultdict(set)
    for first, second in rules:
        page_ordering[first].add(second)

    total_sum = 0

    for update in updates:
        if not is_correct_update(page_ordering, update):
            ordered_update = sort_update(page_ordering, update)
            total_sum += ordered_update[len(ordered_update) // 2]

    return total_sum


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/5"""

    rules, updates = read_input("5.txt")

    print(sum_middle_page_from_correct_updates(rules, updates))
    print(sum_middle_page_from_incorrect_updates(rules, updates))


if __name__ == "__main__":
    solution()
