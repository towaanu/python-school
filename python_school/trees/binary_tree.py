from queue import Queue


def tree_height(tree):
    if tree == None:
        return -1

    left_height = tree_height(tree["left"])
    right_height = tree_height(tree["right"])

    return max(left_height, right_height) + 1


def tree_size(tree):
    if tree == None:
        return 0

    return tree_size(tree['left']) + tree_size(tree['right']) + 1

# Parcours ordre "infix"


def in_order_traversal(tree):
    if tree is None:
        return

    in_order_traversal(tree["left"])
    print(tree["value"])
    in_order_traversal(tree["right"])

# Parcours ordre "suffix"


def post_order_traversal(tree):
    if tree is None:
        return

    post_order_traversal(tree["left"])
    post_order_traversal(tree["right"])
    print(tree["value"])

# Parcours ordre "prefix"


def pre_order_traversal(tree):
    if tree is None:
        return

    print(tree["value"])
    pre_order_traversal(tree["left"])
    pre_order_traversal(tree["right"])

# Parcours en largeur d'abord ( BFS )
# Complexity O(|V| + |E|) <=> O(|V|)
# V = vertices, E = edges
def breadth_first_search(tree):
    nodes_to_visit = Queue()
    nodes_to_visit.put(tree)

    while not nodes_to_visit.empty():
        current_node = nodes_to_visit.get()
        print(current_node['value'])

        if current_node['left'] is not None:
            nodes_to_visit.put(current_node['left'])

        if current_node['right'] is not None:
            nodes_to_visit.put(current_node['right'])


def depth_first_search(tree):
    nodes_to_visit = []
    nodes_to_visit.append(tree)

    while nodes_to_visit:
        current_node = nodes_to_visit.pop()
        print(current_node['value'])


        if current_node['right'] is not None:
            nodes_to_visit.append(current_node['right'])

        if current_node['left'] is not None:
            nodes_to_visit.append(current_node['left'])



if __name__ == "__main__":
    print("hello binary tree :D")

    my_bin_tree = {
        "value": "A",
        "left": {"value": "D",
                 "left": {"value": "E", "left": None, "right": None},
                 "right": {"value": "F", "left": None, "right": None}
                 },
        "right": {
            "value": "B",
            "left": {"value": "G", "left": None, "right": None},
            "right": {"value": "C", "left": None, "right": None}
        }
    }

    # print(tree_height(my_bin_tree))
    # print(tree_size(my_bin_tree))
    # in_order_traversal(my_bin_tree)
    # pre_order_traversal(my_bin_tree)
    # post_order_traversal(my_bin_tree)
    # breadth_first_search(my_bin_tree)
    # depth_first_search(my_bin_tree)
