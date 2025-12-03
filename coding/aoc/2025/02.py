def read_input(file_name: str) -> list[tuple[int, int]]:
    with open(file_name) as file:
        ranges = file.read().strip().split(",")

        result = []
        for id_range in ranges:
            first, second = id_range.split("-")
            result.append((int(first), int(second)))
        return result


def is_invalid_id(id: int) -> bool:
    """
    >>> is_invalid_id(1)
    False
    >>> is_invalid_id(123)
    False
    >>> is_invalid_id(11)
    True
    >>> is_invalid_id(123123)
    True
    """
    str_id = str(id)

    if len(str_id) % 2 == 1:
        return False

    middle = len(str_id) // 2

    return str_id[0:middle] == str_id[middle:]


def is_invalid_id_improved(id: int) -> bool:
    """
    >>> is_invalid_id_improved(999)
    True
    >>> is_invalid_id_improved(565656)
    True
    >>> is_invalid_id_improved(2121212118)
    False
    """
    id_str = str(id)

    n = len(id_str)

    for i in range(1, n):
        tmp = id_str[:i]

        left = id_str[i:]

        # check if all the repetitions match the full length
        if (left.count(tmp) + 1) * len(tmp) == n:
            return True

    return False


def get_invalid_ids_from_range(ids_range: tuple[int, int]) -> list[int]:
    first, last = ids_range

    invalid_ids = []
    for i in range(first, last + 1):
        if is_invalid_id_improved(i):
            invalid_ids.append(i)

    return invalid_ids


def sum_invalid_ids(ranges: list[tuple[int, int]]) -> int:
    total = 0
    for r in ranges:
        total += sum(get_invalid_ids_from_range(r))
    return total


def solution() -> None:
    """Solution to https://adventofcode.com/2025/day/2"""

    print(sum_invalid_ids(read_input("02.txt")))


if __name__ == "__main__":
    solution()
