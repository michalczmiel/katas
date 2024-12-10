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


def calculate_checksum(blocks: list[int]) -> int:
    checksum = 0
    for i, id_number in enumerate(blocks):
        if id_number is not None:
            checksum += i * id_number

    return checksum


def calculate_checksum_when_rearranged_by_blocks(data: str) -> int:
    blocks = generate_blocks(data)

    rearranged = rearrange_by_block(blocks)

    return calculate_checksum(rearranged)


def rearrange_by_word(data: str) -> list[int]:
    blocks = []
    id_number = 0
    is_file = True
    files = []

    for char in data:
        digit = int(char)

        if is_file:
            files.append((id_number, digit, len(blocks)))
            blocks.extend(digit * [id_number])
            id_number += 1
            is_file = False
        else:
            blocks.extend(digit * [None])
            is_file = True

    free_space = 0
    free_space_start = None

    for id_number, needed_space, word_start in reversed(files):
        for i in range(word_start):
            if blocks[i] is None:
                free_space += 1
                if free_space_start is None:
                    free_space_start = i
            else:
                free_space = 0
                free_space_start = None

            if free_space == needed_space:
                for j in range(free_space):
                    blocks[free_space_start + j] = blocks[word_start + j]
                    blocks[word_start + j] = None
                break

    return blocks


def calculate_checksum_when_rearranged_by_words(data: str) -> int:
    rearranged = rearrange_by_word(data)

    return calculate_checksum(rearranged)


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/9"""

    data = read_input("9.txt")
    print(calculate_checksum_when_rearranged_by_blocks(data))
    print(calculate_checksum_when_rearranged_by_words(data))


if __name__ == "__main__":
    solution()
