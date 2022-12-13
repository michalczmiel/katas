def read_input(file_name: str) -> str:
    with open(file_name) as file:
        return file.read()


def get_characters_count_before_unique_sequence(
    buffer: str, sequence_length: int
) -> int:
    right = 0
    left = 0
    unique = set()
    length = len(buffer)

    while left < length:
        if buffer[left] not in unique:
            unique.add(buffer[left])
        else:
            unique.clear()
            right += 1
            left = right

        if len(unique) == sequence_length:
            return left + 1

        left += 1


def solution() -> None:
    """Solution to https://adventofcode.com/2022/day/6"""

    print(
        get_characters_count_before_unique_sequence(
            read_input("input.txt"), sequence_length=4
        )
    )
    print(
        get_characters_count_before_unique_sequence(
            read_input("input.txt"), sequence_length=14
        )
    )


if __name__ == "__main__":
    solution()
