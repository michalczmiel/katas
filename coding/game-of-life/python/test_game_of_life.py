import unittest

from game_of_life import game_of_life

class GameOfLifeTestCase(unittest.TestCase):
    def test_game_of_life(self):
        board = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]

        expected_board = [
            [0, 0, 0],
            [1, 0, 1],
            [0, 1, 1],
            [0, 1, 0]
        ]

        new_board = game_of_life(board)

        self.assertEqual(new_board, expected_board)


if __name__ == '__main__':
    unittest.main()
