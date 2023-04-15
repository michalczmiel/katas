import re
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class PasswordPolicyInput:
    low_number: int
    high_number: int
    letter: str


class PasswordPolicy(ABC):
    @abstractmethod
    def is_password_valid(self, password: str) -> bool:
        pass

    @abstractmethod
    def from_input(cls, input: PasswordPolicyInput) -> "PasswordPolicy":
        pass


@dataclass
class OccurrencePasswordPolicy(PasswordPolicy):
    min_occurrence: int
    max_occurrence: int
    letter: str

    @classmethod
    def from_input(cls, input: PasswordPolicyInput) -> "OccurrencePasswordPolicy":
        return cls(input.low_number, input.high_number, input.letter)

    def is_password_valid(self, password: str) -> bool:
        occurrence_count = password.count(self.letter)
        return self.min_occurrence <= occurrence_count <= self.max_occurrence


@dataclass
class PositionPasswordPolicy(PasswordPolicy):
    letter: str
    positions: list[int]

    @classmethod
    def from_input(cls, input: PasswordPolicyInput) -> "PositionPasswordPolicy":
        return cls(input.letter, [input.low_number, input.high_number])

    def is_password_valid(self, password: str) -> bool:
        positions_containing_letter_count = 0
        for position in self.positions:
            if password[position - 1] == self.letter:
                positions_containing_letter_count += 1

        return positions_containing_letter_count == 1


def read_input() -> list[tuple[PasswordPolicyInput, str]]:
    items = []
    with open("input.txt") as file:
        for line in file:
            low_number, high_number, letter, password = re.findall(r"[a-z0-9]+", line)
            items.append(
                (
                    PasswordPolicyInput(
                        low_number=int(low_number),
                        high_number=int(high_number),
                        letter=letter,
                    ),
                    password,
                )
            )
    return items


def count_correct_passwords(
    items: list[tuple[PasswordPolicyInput, str]], password_policy: PasswordPolicy
) -> int:
    correct_passwords_count = 0

    for policy_input, password in items:
        policy = password_policy.from_input(policy_input)
        if policy.is_password_valid(password):
            correct_passwords_count += 1

    return correct_passwords_count


def solution() -> None:
    """Solution to https://adventofcode.com/2020/day/2"""

    print(count_correct_passwords(read_input(), OccurrencePasswordPolicy))
    print(count_correct_passwords(read_input(), PositionPasswordPolicy))


if __name__ == "__main__":
    solution()
