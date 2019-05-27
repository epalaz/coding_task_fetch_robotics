from classes.exceptions import BoardSizeException, BoardIndexOutOfBoundsException


class Board:

    def __init__(self, row, col):
        if row <= 0 or col <= 0:
            raise BoardSizeException("Invalid row or column size!")

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
        if start_row < 0 or start_row >= self.row or start_col < 0 or start_col >= self.col:
            raise BoardIndexOutOfBoundsException('Invalid index for row or column!')
        self.start_row = start_row
        self.start_col = start_col

    def set_goal(self, goal_row, goal_col):
        if goal_row < 0 or goal_row >= self.row or goal_col < 0 or goal_col >= self.col:
            raise BoardIndexOutOfBoundsException('Invalid index for row or column!')
        self.goal_row = goal_row
        self.goal_col = goal_col

    def set_cost(self, row, col, cost):
        if row < 0 or row >= self.row or col < 0 or col >= self.col:
            raise BoardIndexOutOfBoundsException('Invalid index for row or column!')

        node = self.board[row][col]
        node.cost = cost

    def find_path(self):
        # lets use Djkstra's algorithm while keeping track of all the possible routes
        grid_board = self.board

        if self.start_row == self.goal_row and self.start_col == self.goal_col:
            return {'steps': 1, 'path': [{'i': self.start_row, 'j': self.start_col}]}

        nodes_to_check = []
        visited_nodes = {}

        starting_node = grid_board[self.start_row][self.start_col]

        path_costs = {self.start_row * self.col + self.start_col: 1.0}
        paths = {self.start_row * self.col + self.start_col: [starting_node]}
        nodes_to_check.append(starting_node)

        while len(nodes_to_check) != 0:
            current_node = nodes_to_check.pop()
            current_index = current_node.row * self.col + current_node.col
            neighbor_nodes = []

            if current_node.row >= 1:

                neighbor_node = grid_board[current_node.row - 1][current_node.col]

                new_cost = path_costs[current_index] + neighbor_node.cost
                old_cost = path_costs.get(current_index - self.col, None)
                if old_cost is None or new_cost < old_cost:
                    path_costs[current_index - self.col] = new_cost
                    new_path = paths[current_index].copy()
                    new_path.append(self.board[current_node.row - 1][current_node.col])
                    paths[current_index - self.col] = new_path

                neighbor_nodes.append(neighbor_node)

            if current_node.col >= 1:
                neighbor_node = grid_board[current_node.row][current_node.col - 1]

                new_cost = path_costs[current_index] + neighbor_node.cost
                old_cost = path_costs.get(current_index - 1, None)
                if old_cost is None or new_cost < old_cost:
                    path_costs[current_index - 1] = new_cost
                    new_path = paths[current_index].copy()
                    new_path.append(self.board[current_node.row][current_node.col - 1])
                    paths[current_index - 1] = new_path

                neighbor_nodes.append(neighbor_node)
            if current_node.row < (self.row - 1):
                neighbor_node = grid_board[current_node.row + 1][current_node.col]

                new_cost = path_costs[current_index] + neighbor_node.cost
                old_cost = path_costs.get(current_index + self.col, None)
                if old_cost is None or new_cost < old_cost:
                    path_costs[current_index + self.col] = new_cost
                    new_path = paths[current_index].copy()
                    new_path.append(self.board[current_node.row + 1][current_node.col])
                    paths[current_index + self.col] = new_path

                neighbor_nodes.append(neighbor_node)
            if current_node.col < (self.col - 1):

                neighbor_node = grid_board[current_node.row][current_node.col + 1]

                new_cost = path_costs[current_index] + neighbor_node.cost
                old_cost = path_costs.get(current_index + 1, None)
                if old_cost is None or new_cost < old_cost:
                    path_costs[current_index + 1] = new_cost
                    new_path = paths[current_index].copy()
                    new_path.append(self.board[current_node.row][current_node.col + 1])
                    paths[current_index + 1] = new_path
                neighbor_nodes.append(neighbor_node)

            for neighbor in neighbor_nodes:
                if visited_nodes.get(neighbor.row * self.col + neighbor.col, None) is None:
                    nodes_to_check.append(neighbor)

            visited_nodes[current_index] = current_node

        print("Goal row and col " + str(self.goal_row) + " & " + str(self.goal_col))
        print(path_costs[self.goal_row * self.col + self.goal_col])
        path_to_goal = paths[self.goal_row * self.col + self.goal_col]
        steps = []
        for step in path_to_goal:
            steps.append({'i': step.row, 'j': step.col})

        return {'steps': len(steps), 'path': steps}


class Node:

    def __init__(self, row, col, cost=1.0):
        self.row = row
        self.col = col
        self.cost = cost


def sort_node(val):
    return val.cost
