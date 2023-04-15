import operator
import functools

def read_input() -> list[int]:
    with open("input.txt") as file:
        return [int(line) for line in file]


def calculate_part_one(expenses: list[int]) -> int:
    expected_sum = 2020
    lookup = {}
    
    for expense in expenses:
        existing_pair = lookup.get(expense)
        if existing_pair:
            entries = (existing_pair, expense)

        looking_for = expected_sum - expense

        lookup[looking_for] = expense


    return functools.reduce(operator.mul, entries)


def solution() -> None:
    """Solution to https://adventofcode.com/2020/day/1"""

    print(calculate_part_one(read_input()))


if __name__ == "__main__":
    solution()
