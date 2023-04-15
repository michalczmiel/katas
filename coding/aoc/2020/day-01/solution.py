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


def calculate_part_two(expenses: list[int]) -> int:
    expected_sum = 2020
    match_count = 2
    lookup = {}
    entries = []
    
    for expense in expenses:
        possible_match = lookup.get(expense, [])

        if len(possible_match) == match_count:
            entries = (*possible_match, expense)
            break
        
        lookup_update = {}
        for key, value in lookup.items():
            new_key = key - expense
            if new_key > 0 and len(value) == match_count - 1:
                lookup_update[new_key] = [*value, expense]
        
        lookup.update(lookup_update)
        lookup[expected_sum - expense] = [expense]

    return functools.reduce(operator.mul, entries)    


def solution() -> None:
    """Solution to https://adventofcode.com/2020/day/1"""

    print(calculate_part_one(read_input()))
    print(calculate_part_two(read_input()))


if __name__ == "__main__":
    solution()
