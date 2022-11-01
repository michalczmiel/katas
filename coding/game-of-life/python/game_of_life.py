import copy
from typing import List, NewType, Optional

Board = NewType("Board", List[List[int]])


def get_value(board: Board, x: int, y: int) -> Optional[int]:
    if x < 0 or y < 0:
        return None

    try:
        return board[x][y]
    except IndexError:
        return None


def game_of_life(board: Board) -> Board:
    """
    Given an input of cells as a board calculate the next state
    """
    updated_board = copy.deepcopy(board)

    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            neighbors = [
                get_value(board, x + 1, y),
                get_value(board, x - 1, y),
                get_value(board, x, y + 1),
                get_value(board, x, y - 1),
                get_value(board, x - 1, y - 1),
                get_value(board, x + 1, y + 1),
                get_value(board, x + 1, y - 1),
                get_value(board, x - 1, y + 1),
            ]

            live_neighbors = len([neighbor for neighbor in neighbors if neighbor == 1])

            cell = board[x][y]

            if cell == 1:
                if live_neighbors < 2:
                    updated_board[x][y] = 0
                elif live_neighbors == 2 or live_neighbors == 3:
                    updated_board[x][y] = 1
                else:
                    updated_board[x][y] = 0
            else:
                if live_neighbors == 3:
                    updated_board[x][y] = 1

    return updated_board


