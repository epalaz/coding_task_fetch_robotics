
def get_minimum_cost_elem(node_list):
    min_node = min(node_list, key=min_cost)
    node_list.remove(min_node)
    return min_node


def min_cost(node):
    return node.cost



