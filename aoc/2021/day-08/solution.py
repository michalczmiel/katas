from typing import List, Tuple, NewType

Input = NewType("Input", Tuple[List[str], List[str]])


def read_input() -> List[Input]:
    with open("input.txt") as file:
        output = []

        for line in file.readlines():
            unique_signals, digit_output_values = line.strip().split(" | ")
            output.append((unique_signals.split(" "), digit_output_values.split(" ")))
        return output


def count_digits_1_4_7_8(output_values_list: List[Input]) -> int:
    digit_length_mapping = {1: 2, 4: 4, 7: 3, 8: 7}

    count = 0
    for segments, digits in output_values_list:
        length_segment_mapping = {}
        for segment in segments:
            length = len(segment)
            if length in digit_length_mapping.values():
                length_segment_mapping[length] = segment

        for digit in digits:
            segment = length_segment_mapping.get(len(digit))

            if segment:
                count += 1
    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/8"""

    print(count_digits_1_4_7_8(read_input()))


if __name__ == "__main__":
    solution()
