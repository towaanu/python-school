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


if __name__ == "__main__":
    print("hello binary tree :D")

    my_bin_tree = {
        "value": "A",
        "left": {"value": "D", "left": None, "right": None},
        "right": {
            "value": "B",
            "left": None,
            "right": {"value": "C", "left": None, "right": None}
        }
    }

    print(tree_height(my_bin_tree))
    print(tree_size(my_bin_tree))
