from collections import defaultdict


def read_input(file_name: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
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


def is_correct_update(page_ordering: dict[int, set], update: list[int]) -> bool:
    for i in range(1, len(update)):
        for j in range(0, i):
            previous_number = update[j]
            number = update[i]

            numbers_after = page_ordering.get(number, set())
            if previous_number in numbers_after:
                return False

    return True


def sum_middle_page_from_correct_updates(
    rules: list[tuple[int, int]], updates: list[list[int]]
) -> int:
    page_ordering = defaultdict(set)
    for first, second in rules:
        page_ordering[first].add(second)

    total_sum = 0

    for update in updates:
        if is_correct_update(page_ordering, update):
            total_sum += update[len(update) // 2]

    return total_sum


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/5"""

    rules, updates = read_input("5.txt")

    print(sum_middle_page_from_correct_updates(rules, updates))


if __name__ == "__main__":
    solution()
