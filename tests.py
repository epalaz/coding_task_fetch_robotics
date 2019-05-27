from classes.board import Board


def test_board():
    board = Board(5, 5)
    board.set_start(0, 0)
    board.set_goal(3, 3)
    board.set_cost(0, 1, 10.0)
    board.set_cost(1, 1, 10.0)
    board.set_cost(2, 1, 10.0)
    board.set_cost(2, 2, 10.0)
    board.set_cost(2, 3, 10.0)
    board.set_cost(2, 4, 10.0)
    print(board.find_path())
