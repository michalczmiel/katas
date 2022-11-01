import copy
from typing import List, NewType, Optional

State = NewType("State", int)
Board = NewType("Board", List[List[State]])

ALIVE: State = 1
DEAD: State = 0
# each cell interacts with eight neighbors (horizontal, vertical, diagonal)
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]


def get_value(board: Board, x: int, y: int) -> Optional[State]:
    """
    Get single cell for given indexes or None if out of range
    """
    if x < 0 or y < 0:
        return None
    try:
        return board[x][y]
    except IndexError:
        return None


def game_of_life(board: Board) -> Board:
    """
    Given an input of cells as a board, calculate the next state
    """
    if not board:
        raise Exception("Empty board")

    updated_board = copy.deepcopy(board)

    m = len(board)
    n = len(board[0])

    for x in range(m):
        for y in range(n):
            neighbors = (get_value(board, x + dx, y + dy) for dx, dy in DIRECTIONS)
            live_neighbors = len([neighbor for neighbor in neighbors if neighbor == 1])

            state = board[x][y]

            if state == ALIVE:
                if live_neighbors < 2:
                    updated_board[x][y] = DEAD
                elif live_neighbors == 2 or live_neighbors == 3:
                    updated_board[x][y] = ALIVE
                else:
                    updated_board[x][y] = DEAD
            else:
                if live_neighbors == 3:
                    updated_board[x][y] = ALIVE

    return updated_board
