def read_input(file_name: str) -> str:
    with open(file_name) as file:
        return file.read().strip()


def generate_blocks(data: str) -> list[int]:
    blocks = []

    id_number = 0
    is_file = True

    for char in data:
        digit = int(char)

        if is_file:
            blocks.extend(digit * [id_number])
            id_number += 1
            is_file = False
        else:
            blocks.extend(digit * [None])
            is_file = True

    return blocks


def rearrange_by_block(blocks: list[int]) -> list[int]:
    rearranged = blocks.copy()

    l = 0
    r = len(rearranged) - 1

    while True:
        while rearranged[l] is not None and l < r:
            l += 1

        if l == r:
            break

        rearranged[l] = rearranged[r]
        rearranged[r] = None
        r -= 1

    return rearranged


def calculate_checksum(data: str) -> int:
    blocks = generate_blocks(data)

    rearranged = rearrange_by_block(blocks)

    checksum = 0
    for i, id_number in enumerate(rearranged):
        if id_number is not None:
            checksum += i * id_number

    return checksum


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/9"""

    data = read_input("9.txt")
    print(calculate_checksum(data))


if __name__ == "__main__":
    solution()
