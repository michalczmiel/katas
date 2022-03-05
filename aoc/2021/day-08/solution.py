from typing import List, Tuple, NewType, Final

Input = NewType("Input", Tuple[List[str], List[str]])


DIGIT_LENGTH_MAPPING: Final = {1: 2, 4: 4, 7: 3, 8: 7}

LENGTH_DIGIT_MAPPING: Final = {
    2: 1,
    3: 7,
    4: 4,
    5: {2, 3, 5},
    6: {0, 6, 9},
    7: 8,
}


def read_input() -> List[Input]:
    with open("input.txt") as file:
        output = []

        for line in file.readlines():
            unique_signals, digit_output_values = line.strip().split(" | ")
            output.append((unique_signals.split(" "), digit_output_values.split(" ")))
        return output


def count_digits_1_4_7_8(list_of_inputs: List[Input]) -> int:
    count = 0
    for segments, digits in list_of_inputs:
        length_segment_mapping = {}
        for segment in segments:
            length = len(segment)
            if length in DIGIT_LENGTH_MAPPING.values():
                length_segment_mapping[length] = segment

        for digit in digits:
            segment = length_segment_mapping.get(len(digit))

            if segment:
                count += 1
    return count


def count_output_values_sum(list_of_inputs: List[Input]) -> int:
    total_sum = 0
    for digit_signals, digits in list_of_inputs:
        one_signals = next(
            set(signal)
            for signal in digit_signals
            if len(signal) == DIGIT_LENGTH_MAPPING[1]
        )
        four_signals = next(
            set(signal)
            for signal in digit_signals
            if len(signal) == DIGIT_LENGTH_MAPPING[4]
        )

        signal_mapping = {}
        for digit_signal in digit_signals:
            digit = LENGTH_DIGIT_MAPPING.get(len(digit_signal))

            found_digit = digit if isinstance(digit, int) else None
            signal_elements = set(digit_signal)

            one_intersections_count = len(signal_elements.intersection(one_signals))
            four_intersections_count = len(signal_elements.intersection(four_signals))

            digit_intersection_mapping = {
                2: one_intersections_count == 1 and four_intersections_count == 2,
                3: one_intersections_count == 2,
                5: one_intersections_count == 1 and four_intersections_count == 3,
                0: one_intersections_count == 2 and four_intersections_count == 3,
                6: one_intersections_count == 1,
                9: four_intersections_count == 4,
            }

            if not found_digit:
                for possible_digit in digit:
                    if digit_intersection_mapping[possible_digit]:
                        found_digit = possible_digit

            key = "".join(sorted(signal_elements))
            signal_mapping[key] = found_digit

        output = ""
        for digit in digits:
            key = "".join(sorted(digit))
            value = signal_mapping[key]
            output += str(value)

        total_sum += int(output)

    return total_sum


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/8"""

    print(count_digits_1_4_7_8(read_input()))
    print(count_output_values_sum(read_input()))


if __name__ == "__main__":
    solution()
