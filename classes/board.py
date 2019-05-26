

class Board:

    def __init__(self, row, col):
        board = []
        for r in range(0, row):
            board_row = []
            for c in range(0, col):
                node = Node(row=r, col=c)
                board_row.append(node)
            board.append(board_row)
        self.row = row
        self.col = col
        self.board = board
        self.start_row = None
        self.start_col = None
        self.goal_row = None
        self.goal_col = None

    def set_start(self, start_row, start_col):
        self.start_row = start_row
        self.start_col = start_col

    def set_goal(self, goal_row, goal_col):
        self.goal_row = goal_row
        self.goal_col = goal_col

    def set_cost(self, row, col, cost):
        node = self.board[row][col]
        node.cost = cost

    def find_path(self):
        # lets use djkstra's algorithm
        return {'steps': 1, 'path': []}


class Node:

    def __init__(self, row, col, cost=0.0):
        self.row = row
        self.col = col
        self.cost = cost
