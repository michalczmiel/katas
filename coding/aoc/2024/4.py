def read_input(file_name: str) -> list[list[str]]:
    with open(file_name) as f:
        return [[char for char in line.strip()] for line in f]


WORD = "XMAS"
WORD_IN_REVERSE = "".join(reversed(WORD))
INVOLVED_LETTERS = set(WORD)


def find_horizontal(x: int, y: int, words: list[list[str]]) -> bool:
    try:
        found = ""
        for i in range(y, y + len(WORD)):
            found += words[x][i]

        return found == WORD or found == WORD_IN_REVERSE
    except IndexError:
        return False


def find_vertical(x: int, y: int, words: list[list[str]]) -> bool:
    try:
        found = ""
        for i in range(x, x + len(WORD)):
            found += words[i][y]

        return found == WORD or found == WORD_IN_REVERSE
    except IndexError:
        return False


def count_diagonal(x: int, y: int, words: list[list[str]]) -> int:
    directions_combinations = {(1, 1), (-1, 1), (1, -1), (-1, -1)}
    count = 0

    for directions in directions_combinations:
        found = ""
        new_x = x
        new_y = y

        try:
            path = ""
            found = ""
            for _ in range(len(WORD)):
                # negative indexes are accepted by Python, we need to filter them out
                if new_y < 0 or new_x < 0:
                    break

                path += str(new_x) + str(new_y)
                found += words[new_x][new_y]

                new_y += directions[1]
                new_x += directions[0]

            if found == WORD:
                count += 1
        except IndexError:
            continue

    return count


def count_xmas_occurrences(words: list[list[str]]) -> int:
    count = 0

    for x in range(len(words)):
        for y in range(len(words[x])):
            char = words[x][y]

            if char not in INVOLVED_LETTERS:
                continue

            if find_horizontal(x, y, words):
                count += 1

            if find_vertical(x, y, words):
                count += 1

            count += count_diagonal(x, y, words)

    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/4"""

    data = read_input("4.txt")

    print(count_xmas_occurrences(data))


if __name__ == "__main__":
    solution()
