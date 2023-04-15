import re
from dataclasses import dataclass


@dataclass
class PasswordPolicy:
    letter: str
    min_occurence: int
    max_occurence: int

    def is_password_valid(self, password: str):
        occurence_count = password.count(self.letter)
        return self.min_occurence <= occurence_count <= self.max_occurence


def read_input() -> list[PasswordPolicy, str]:
    items = []
    with open("input.txt") as file:
        for line in file:
            min_occurence, max_occurence, letter, password = re.findall(
                r"[a-z0-9]+", line
            )
            items.append(
                [
                    PasswordPolicy(
                        min_occurence=int(min_occurence),
                        max_occurence=int(max_occurence),
                        letter=letter,
                    ),
                    password,
                ]
            )
    return items


def count_correct_passwords(items: list[PasswordPolicy, str]) -> int:
    correct_passwords_count = 0

    for password_policy, password in items:
        correct_passwords_count += password_policy.is_password_valid(password)

    return correct_passwords_count


def solution() -> None:
    """Solution to https://adventofcode.com/2020/day/2"""

    print(count_correct_passwords(read_input()))


if __name__ == "__main__":
    solution()
