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
