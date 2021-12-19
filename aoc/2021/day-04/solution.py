from typing import List, Tuple


class Board:
    def __init__(self, numbers: List[List[int]]) -> None:
        self._numbers = numbers
        self._n = len(numbers)
        self._marked = [[False] * 5 for _ in range(self._n)]

    def draw_number(self, new_number: int) -> None:
        for x in range(self._n):
            for y in range(self._n):
                if self._numbers[x][y] == new_number:
                    self._marked[x][y] = True

    def _has_row_completed(self) -> bool:
        for row in self._marked:
            if all(row):
                return True
        return False

    def _has_column_completed(self) -> bool:
        for y in range(self._n):
            if all(self._marked[x][y] for x in range(self._n)):
                return True
        return False

    def has_won(self) -> bool:
        return self._has_row_completed() or self._has_column_completed()

    def get_unmarked_sum(self) -> int:
        unmarked = []

        for x in range(self._n):
            for y in range(self._n):
                if self._marked[x][y] == 0:
                    unmarked.append(self._numbers[x][y])

        return sum(unmarked)


def read_input() -> Tuple[List[int], List[List[int]]]:
    with open("input.txt") as file:
        numbers = [int(number) for number in file.readline().strip().split(",")]

        file.readline()

        boards = []
        board = []

        for line in file.readlines():
            if line == "\n":
                boards.append(board.copy())
                board.clear()
            else:
                board.append([int(x) for x in line.strip().split(" ") if x])

        return numbers, boards


def get_winning_board_and_number(
    inputs: List[int], boards: List[List[int]]
) -> Tuple[Board, int]:
    game_boards = [Board(board) for board in boards]

    for number in inputs:
        for board in game_boards:
            board.draw_number(number)
            if board.has_won():
                return board, number


def get_winning_board_final_score(input: Tuple[List[int], List[List[int]]]) -> int:
    numbers, boards = input

    board, number = get_winning_board_and_number(numbers, boards)

    unmarked_sum = board.get_unmarked_sum()

    return number * unmarked_sum


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/4"""

    print(get_winning_board_final_score(read_input()))


if __name__ == "__main__":
    solution()
