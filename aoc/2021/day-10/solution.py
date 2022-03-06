from typing import List, Optional, Tuple
from collections import deque

Input = List[List[str]]


def read_input() -> Input:
    lines = []
    with open("input.txt") as file:
        for line in file.readlines():
            lines.append(line.strip())
    return lines


CHAR_ENDING_MAPPING = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def get_first_illegal_char_and_expected_chars(line: str) -> Tuple[Optional[str], deque]:
    expected_chars = deque()
    for char in line:
        ending = CHAR_ENDING_MAPPING.get(char)

        if ending:
            expected_chars.append(ending)
            continue

        expected_ending = expected_chars.pop()
        if char != expected_ending:
            return char, expected_chars
    return None, expected_chars


def get_expected_chars(line: str) -> deque:
    expected_chars = deque()
    for char in line:
        ending = CHAR_ENDING_MAPPING.get(char)

        if ending:
            expected_chars.append(ending)
            continue
        expected_chars.pop()
    return expected_chars


def calculate_first_illegal_chars_score(lines: Input) -> int:
    first_illegal_chars = []
    for line in lines:
        illegal_char, _ = get_first_illegal_char_and_expected_chars(line)
        if illegal_char:
            first_illegal_chars.append(illegal_char)

    char_score_mapping = {")": 3, "]": 57, "}": 1197, ">": 25137}

    score = sum(char_score_mapping[char] for char in first_illegal_chars)

    return score


def calculate_autocomplete_score(lines: Input) -> int:
    char_score_mapping = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    scores = []
    for line in lines:
        score = 0

        illegal_char, expected_chars = get_first_illegal_char_and_expected_chars(line)
        if illegal_char:
            continue

        for char in reversed(expected_chars):
            score *= 5
            score += char_score_mapping[char]

        if score:
            scores.append(score)

    sorted_scores = sorted(scores)
    # there will always be an odd number of scores to consider
    middle_index = (len(sorted_scores) - 1) // 2
    return sorted_scores[middle_index]


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/10"""

    print(calculate_first_illegal_chars_score(read_input()))
    print(calculate_autocomplete_score(read_input()))


if __name__ == "__main__":
    solution()
