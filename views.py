from flask import request, jsonify
from classes.board import Board

# shared status of the game is held in a variable
board = None


def index():
    return "Hello World", 200


def create_map():
    body = request.json
    row = body.get('row', None)
    col = body.get('col', None)
    if row is None or col is None:
        return jsonify({'error': 'Either \'row\' or \'col\' parameter is missing!'}), 400

    if not isinstance(row, int) or not isinstance(col, int):
        return jsonify({'error': 'Both \'col\' and \'row\' should be integers!'}), 400

    if row <= 0 and col <= 0:
        return jsonify({'error': 'Both \'col\' and \'row\' should be larger than 0!'}), 400

    global board
    board = Board(row, col)

    return jsonify({'row': row, 'col': col}), 201


def create_start():
    global board

    if board is None:
        return jsonify({'error': 'Board doesn\'t exist! Please create a board by using \'/api/maps/\' endpoint!'}), 400

    body = request.json
    i = body.get('i', None)
    j = body.get('j', None)
    if i is None or j is None:
        return jsonify({'error': 'Either \'i\' or \'j\' parameter is missing!'}), 400

    if not isinstance(i, int) or not isinstance(j, int):
        return jsonify({'error': 'Both \'i\' and \'j\' should be integers!'}), 400

    if i < 0 and j < 0:
        return jsonify({'error': 'Both \'i\' and \'j\' should be equal or larger than 0!'}), 400

    if i >= board.row or j >= board.col:
        return jsonify({'error': 'Both \'col\' and \'row\' indexes should be smaller than row and column of current '
                                 'board!'}), 400

    board.set_start(start_row=i, start_col=j)

    return jsonify({'i': i, 'j': j}), 201


def create_goal():
    global board

    if board is None:
        return jsonify({'error': 'Board doesn\'t exist! Please create a board by using \'/api/maps/\' endpoint!'}), 400

    body = request.json
    i = body.get('i', None)
    j = body.get('j', None)
    if i is None or j is None:
        return jsonify({'error': 'Either \'i\' or \'j\' parameter is missing!'}), 400

    if not isinstance(i, int) or not isinstance(j, int):
        return jsonify({'error': 'Both \'i\' and \'j\' should be integers!'}), 400

    if i < 0 and j < 0:
        return jsonify({'error': 'Both \'i\' and \'j\' should be equal or larger than 0!'}), 400

    if i >= board.row or j >= board.col:
        return jsonify({'error': 'Both \'col\' and \'row\' indexes should be smaller than row and column of current '
                                 'board!'}), 400

    board.set_goal(start_row=i, start_col=j)

    return jsonify({'i': i, 'j': j}), 201


def create_heuristic_cost():
    global board

    if board is None:
        return jsonify({'error': 'Board doesn\'t exist! Please create a board by using \'/api/maps/\' endpoint!'}), 400

    body = request.json
    costs = body.get('costs', None)

    print(type(costs))

    if costs is None:
        return jsonify({'error': 'Either costs field is missing!'}), 400

    if isinstance(costs, list):
        return jsonify({'error': 'Costs should be a dict of i, j and cost fields!'}), 400

    if len(costs) == 0:
        return jsonify({'error': 'Costs list is empty!'}), 400

    # first check validity of elements to avoid the need for a rollback
    for cost in costs:
        i = cost.get('i', None)
        j = cost.get('j', None)
        value = cost.get('value', None)

        if i is None or j is None or value is None:
            return jsonify({'error': 'Missing field in a cost! Cost should have fields \'i\', \'j\' and \'value\'!'}), 400

        if not isinstance(i, int) or not isinstance(j, int):
            return jsonify({'error': 'Both \'i\' and \'j\' should be integers!'}), 400

        if i < 0 and j < 0:
            return jsonify({'error': 'Both \'i\' and \'j\' should be equal or larger than 0!'}), 400

        if i >= board.row or j >= board.col:
            return jsonify(
                {'error': 'Both \'col\' and \'row\' indexes should be smaller than row and column of current '
                          'board!'}), 400

        if not isinstance(value, float):
            return jsonify({'error': '\'value\' field should be a float!'}), 400

        if value < 0.0:
            return jsonify({'error': '\'value\' field should be a larger than 0!'}), 400

    for cost in costs:
        i = cost.get('i', None)
        j = cost.get('j', None)
        value = cost.get('value', None)

        board.set_cost(i, j, value)

    return jsonify({'costs': costs}), 201


def find_path():
    global board

    output = board.find_path()

    return jsonify(output), 200
