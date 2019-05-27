import unittest
from classes.board import Board, Node
from classes.exceptions import BoardSizeException, BoardIndexOutOfBoundsException

medium_map = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0]
]

class BoardTestCase(unittest.TestCase):

    def setUp(self):
        self.board = Board(10, 10)

    def test_node_initialization(self):
        node = Node(1, 5, 10.0)
        self.assertEqual(node.row, 1)
        self.assertEqual(node.col, 5)
        self.assertEqual(node.cost, 10.0)

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

    def test_set_cost(self):
        self.board.set_cost(0, 0, 20.0)
        self.board.set_cost(3, 4, 15.3)

        self.assertEqual(self.board.board[0][0].cost, 20.0)
        self.assertEqual(self.board.board[3][4].cost, 15.3)

    def test_find_path_equal_start_goal(self):
        self.board.set_start(3, 8)
        self.board.set_goal(3, 8)
        self.board.set_cost(2, 9, 90.0)
        path = self.board.find_path()
        self.assertEqual(path['steps'], 1)
        self.assertEqual(len(path['path']), 1)
        self.assertEqual(path['path'][0]['i'], 3)
        self.assertEqual(path['path'][0]['j'], 8)

    def test_find_path_medium(self):
        board = Board(5, 5)
        board.set_start(0, 0)
        board.set_goal(2, 2)
        for row in range(len(medium_map)):
            for col in range(len(medium_map[0])):
                if medium_map[row][col] == 1:
                    print((row, col))
                    board.set_cost(row, col, 100.0)
        result = board.find_path()
        print(result['path'])
        self.assertEqual(result['steps'], 11)


if __name__ == '__main__':
    unittest.main()
