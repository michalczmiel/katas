from typing import List, Optional
from collections import deque

Input = List[List[str]]


def read_input() -> Input:
    lines = []
    with open("input.txt") as file:
        for line in file.readlines():
            lines.append(line.strip())
    return lines


def get_first_illegal_char(line: str) -> Optional[str]:
    char_ending_mapping = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    expected_chars = deque()
    for char in line:
        ending = char_ending_mapping.get(char)

        if ending:
            expected_chars.append(ending)
            continue

        expected_ending = expected_chars.pop()
        if char != expected_ending:
            return char


def count_first_illegal_chars_score(lines: Input) -> int:
    first_illegal_chars = []
    for line in lines:
        illegal_char = get_first_illegal_char(line)
        if illegal_char:
            first_illegal_chars.append(illegal_char)

    char_score_mapping = {")": 3, "]": 57, "}": 1197, ">": 25137}

    score = sum(char_score_mapping[char] for char in first_illegal_chars)

    return score


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/10"""

    print(count_first_illegal_chars_score(read_input()))


if __name__ == "__main__":
    solution()
