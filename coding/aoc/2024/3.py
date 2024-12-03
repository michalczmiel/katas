import re


def read_input(file_name: str) -> str:
    with open(file_name) as f:
        return f.read()


def sum_of_multiplications(data: str) -> int:
    result = 0

    operations = re.findall(r"mul\(\d+,\d+\)", data)

    for operation in operations:
        first, second = re.findall(r"\d+", operation)

        result += int(first) * int(second)

    return result


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/3"""

    data = read_input("3.txt")

    print(sum_of_multiplications(data))


if __name__ == "__main__":
    solution()
