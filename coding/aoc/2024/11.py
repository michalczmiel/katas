import collections


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


def get_stones_count(initial: list[int], blinks: int) -> list[int]:
    stone_count = collections.defaultdict(int)

    for number in initial:
        stone_count[number] = 1

    for _ in range(blinks):
        updated_count = stone_count.copy()

        for number, count in stone_count.items():
            if count == 0:
                continue

            if number == 0:
                updated_count[1] += count
            else:
                splitted = split_even_digit_number(number)
                if splitted is None:
                    updated_count[number * 2024] += count
                else:
                    first, second = splitted
                    updated_count[first] += count
                    updated_count[second] += count

            updated_count[number] -= count

        stone_count = updated_count

    return sum(stone_count.values())


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/11"""

    data = read_input("11.txt")
    print(get_stones_count(data, blinks=25))
    print(get_stones_count(data, blinks=75))


if __name__ == "__main__":
    solution()
