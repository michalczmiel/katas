from collections import defaultdict, Counter
from typing import Dict, List, Optional


def read_input() -> List[str]:
    with open("input.txt") as file:
        return list(line.strip() for line in file.readlines())


def calculate_power_consumption(diagnostic: List[str]) -> int:
    counts = defaultdict(lambda: {"0": 0, "1": 0})

    for number in diagnostic:
        for index in range(12):
            counts[index][number[index]] += 1

    gamma_rate_binary = ""
    epsilon_rate_binary = ""

    for count in counts.values():
        if count["1"] > count["0"]:
            gamma_rate_binary += "1"
            epsilon_rate_binary += "0"
        else:
            gamma_rate_binary += "0"
            epsilon_rate_binary += "1"

    gamma_rate = int(gamma_rate_binary, 2)
    epsilon_rate = int(epsilon_rate_binary, 2)

    return gamma_rate * epsilon_rate


def get_most_common(counts: Dict[str, int]) -> Optional[str]:
    if counts["0"] == counts["1"]:
        return None

    return "0" if counts["0"] > counts["1"] else "1"


def get_least_common(counts: Dict[str, int]) -> Optional[str]:
    if counts["0"] == counts["1"]:
        return None

    return "1" if counts["0"] > counts["1"] else "0"


def filter_numbers(
    index: int, numbers: List[str], expected_value: Optional[str], second_best: str
) -> List[str]:
    filtered_numbers = []

    for number in numbers:
        if number[index] == expected_value or (
            not expected_value and number[index] == second_best
        ):
            filtered_numbers.append(number)

    return filtered_numbers


def get_rating_by_criteria(numbers: List[str], criteria: str) -> str:
    found_numbers = numbers.copy()

    if criteria == "most":
        get_expected_value = get_most_common
        second_best = "1"
    else:
        get_expected_value = get_least_common
        second_best = "0"

    for index in range(12):
        bit_counts_per_index = Counter(number[index] for number in found_numbers)
        expected_value = get_expected_value(bit_counts_per_index)

        found_numbers = filter_numbers(
            index, found_numbers, expected_value, second_best
        )
        if len(found_numbers) == 1:
            return found_numbers[0]


def calculate_life_support_rating(diagnostic: List[str]) -> int:
    oxygen_generator_rating_binary = get_rating_by_criteria(diagnostic, criteria="most")
    co2_scrubber_rating_binary = get_rating_by_criteria(diagnostic, criteria="least")

    return int(oxygen_generator_rating_binary, 2) * int(co2_scrubber_rating_binary, 2)


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/3"""

    print(calculate_power_consumption(read_input()))
    print(calculate_life_support_rating(read_input()))


if __name__ == "__main__":
    solution()
