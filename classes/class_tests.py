import unittest
from classes.board import Board, Node
from classes.exceptions import BoardSizeException, BoardIndexOutOfBoundsException


class BoardTestCase(unittest.TestCase):

    def setUp(self):
        self.board = Board(10, 10)

    def test_board_initialization(self):
        board = Board(5, 5)
        self.assertEqual(board.row, 5)
        self.assertEqual(board.col, 5)
        self.assertEqual(len(board.board), 5)
        for row in board.board:
            self.assertEqual(len(row), 5)

    def test_board_size_invalid_exception(self):
        self.assertRaises(BoardSizeException, Board, -1, 10)

    def test_set_start(self):
        self.board.set_start(3, 4)
        self.assertEqual(self.board.start_row, 3)
        self.assertEqual(self.board.start_col, 4)

    def test_set_start_invalid_index(self):
        self.assertRaises(BoardIndexOutOfBoundsException, self.board.set_start, 30, -10)

    def test_set_goal(self):
        self.board.set_goal(6, 9)
        self.assertEqual(self.board.goal_row, 6)
        self.assertEqual(self.board.goal_col, 9)

    def test_set_goal_invalid_index(self):
        self.assertRaises(BoardIndexOutOfBoundsException, self.board.set_goal, -10, -10)


if __name__ == '__main__':
    unittest.main()
