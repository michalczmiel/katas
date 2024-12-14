def read_input(file_name: str) -> list[int]:
    with open(file_name) as file:
        return [int(number) for number in file.read().strip().split(" ")]


def split_even_digit_number(number: int) -> tuple[int, int] | None:
    str_number = str(number)
    length = len(str_number)

    if length % 2 != 0:
        return None

    middle = length // 2

    first = int(str_number[:middle])
    second = int(str_number[middle:])

    return (first, second)


def simulate_stones(initial: list[int], blinks: int) -> list[int]:
    processing = initial

    for _ in range(blinks):
        updated = []

        for number in processing:
            if number == 0:
                updated.append(1)
                continue

            splitted_number = split_even_digit_number(number)
            if splitted_number is None:
                updated.append(number * 2024)
            else:
                updated.append(splitted_number[0])
                updated.append(splitted_number[1])

        processing = updated

    return processing


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/11"""

    data = read_input("11.txt")
    print(len(simulate_stones(data, blinks=25)))


if __name__ == "__main__":
    solution()
