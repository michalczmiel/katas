from collections import Counter
from typing import NewType

Question = NewType("Question", str)


def read_input() -> list[list[Question]]:
    with open("input.txt") as file:
        groups = []
        current_group = []

        for line in file:
            line = line.strip()

            if line:
                current_group.append(line)
            else:
                groups.append([*current_group])
                current_group.clear()

        groups.append(current_group)

        return groups


def count_yes_answers(groups: list[list[Question]]) -> int:
    yes_answers = 0

    for group in groups:
        counter = Counter()
        for questions in group:
            counter.update(questions)
        yes_answers += len(counter.keys())

    return yes_answers


def solution() -> None:
    """Solution to https://adventofcode.com/2020/day/6"""

    print(count_yes_answers(read_input()))


if __name__ == "__main__":
    solution()
