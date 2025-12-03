def read_input(file_name: str):
    with open(file_name) as file:
        for line in file:
            line = line.strip()
            if line:
                yield line


def calculate_largest_joltage_possible(bank: str) -> int:
    """
    >>> calculate_largest_joltage_possible("987654321111111")
    98
    >>> calculate_largest_joltage_possible("811111111111119")
    89
    """

    n = len(bank)

    biggest = [0] * n

    max_digit = 0

    for i in range(n - 1, 0, -1):
        max_digit = max(int(bank[i]), max_digit)
        biggest[i - 1] = max_digit

    joltage = set()

    for i in range(n):
        digit = int(bank[i])

        if biggest[i] == 0:
            continue

        joltage.add(int(f"{digit}{biggest[i]}"))

    return max(joltage)


def calculate_total_output(banks) -> int:
    return sum(calculate_largest_joltage_possible(bank) for bank in banks)


def solution() -> None:
    """Solution to https://adventofcode.com/2025/day/3"""

    print(calculate_total_output(read_input("03.txt")))


if __name__ == "__main__":
    solution()
