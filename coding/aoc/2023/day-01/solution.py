from typing import Iterator


def read_input(file_name: str) -> Iterator[str]:
    with open(file_name, "r") as file:
        for line in file:
            yield line


# first and last letters are saved so overlapping words are correctly detected
WRITTEN_DIGITS_REPLACEMENT_MAPPING = {
    "one": "o1e",
    "two": "t2o",
    "three": "th3ee",
    "four": "fo4ur",
    "five": "fi5ve",
    "six": "s6x",
    "seven": "se7en",
    "eight": "ei8ht",
    "nine": "ni9ne",
}


def get_calibration_value(line: str) -> int:
    """
    Extracts the first and last digit and transforms it to number.
    Works also on digits in the word form
    """
    line_with_digits = line

    for word, replacement in WRITTEN_DIGITS_REPLACEMENT_MAPPING.items():
        line_with_digits = line_with_digits.replace(word, replacement)

    digits = [char for char in line_with_digits if char.isdigit()]

    if len(digits) == 1:
        first_digit, second_digit = digits[0], digits[0]
    else:
        first_digit, second_digit = digits[0], digits[-1]

    number = int(f"{first_digit}{second_digit}")

    return number


def process_calibration_document(lines: str) -> int:
    return sum(get_calibration_value(line) for line in lines)


def solution() -> None:
    """Solution to https://adventofcode.com/2023/day/1"""

    print(process_calibration_document(read_input("input.txt")))


if __name__ == "__main__":
    solution()
