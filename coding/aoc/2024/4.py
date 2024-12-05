from typing import NewType

Words = NewType("Words", list[list[str]])


def read_input(file_name: str) -> Words:
    with open(file_name) as f:
        return [[char for char in line.strip()] for line in f]


WORD = "XMAS"
WORD_IN_REVERSE = "".join(reversed(WORD))
INVOLVED_LETTERS = set(WORD)


def find_horizontal(words: Words, x: int, y: int) -> bool:
    try:
        found = ""
        for i in range(y, y + len(WORD)):
            found += words[x][i]

        return found == WORD or found == WORD_IN_REVERSE
    except IndexError:
        return False


def find_vertical(words: Words, x: int, y: int) -> bool:
    try:
        found = ""
        for i in range(x, x + len(WORD)):
            found += words[i][y]

        return found == WORD or found == WORD_IN_REVERSE
    except IndexError:
        return False


def count_diagonal(words: Words, x: int, y: int) -> int:
    directions_combinations = {(1, 1), (-1, 1), (1, -1), (-1, -1)}
    count = 0

    for directions in directions_combinations:
        found = ""
        new_x = x
        new_y = y

        try:
            found = ""
            for _ in range(len(WORD)):
                # negative indexes are accepted by Python, we need to filter them out
                if new_y < 0 or new_x < 0:
                    break

                found += words[new_x][new_y]
                new_y += directions[1]
                new_x += directions[0]

            if found == WORD:
                count += 1
        except IndexError:
            continue

    return count


def count_xmas_occurrences(words: Words) -> int:
    count = 0

    for x in range(len(words)):
        for y in range(len(words[x])):
            char = words[x][y]

            if char not in INVOLVED_LETTERS:
                continue

            if find_horizontal(words, x, y):
                count += 1

            if find_vertical(words, x, y):
                count += 1

            count += count_diagonal(words, x, y)

    return count


def check_if_x_shape(words: Words, x: int, y: int) -> bool:
    diagonal_positions = [
        [(x - 1, y - 1), (x, y), (x + 1, y + 1)],
        [(x - 1, y + 1), (x, y), (x + 1, y - 1)],
    ]

    try:
        found_words = []
        for positions in diagonal_positions:
            word = ""
            for (
                px,
                py,
            ) in positions:
                if px < 0 or py < 0:
                    continue

                word += words[px][py]

            found_words.append(word)

        return found_words.count("SAM") + found_words.count("MAS") == 2
    except IndexError:
        return False


def count_x_mas_occurrences(words: list[list[str]]) -> int:
    count = 0

    for x in range(len(words)):
        for y in range(len(words[x])):
            char = words[x][y]

            if char not in INVOLVED_LETTERS or char == "X":
                continue

            if check_if_x_shape(words, x, y):
                count += 1

    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/4"""

    data = read_input("4.txt")

    print(count_xmas_occurrences(data))
    print(count_x_mas_occurrences(data))


if __name__ == "__main__":
    solution()
