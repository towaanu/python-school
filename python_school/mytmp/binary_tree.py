
def create_binary_search_tree(init_value):
    return {'value': init_value, 'left': None, 'right': None}

# def insert_value(node, value):

#     if node is None:
#         return {'value': value, 'left': None, 'right': None}

#     elif value < node["value"]:
#         insert_value(node["left"], value)

#     else:
#         insert_value(node["right"], value)


def insert_value(node, value):

    if node is None:
        return {'value': value, 'left': None, 'right': None}

    elif value < node["value"]:
        if node["left"] is None:
            node["left"] = {'value': value, 'left': None, 'right': None}
        else:
            insert_value(node["left"], value)
    
    elif value > node["value"]:
        if node["right"] is None:
            node["right"] = {'value': value, 'left': None, 'right': None}
        else:
            insert_value(node["right"], value)

# Prefix/Preordre/Preorder
def visit_prefix(tree):
    if tree is None:
        return

    print(f"Prefix: {tree['value']}")
    visit_prefix(tree['left'])
    visit_prefix(tree['right'])

# Postfix/suffix/postordre
def visit_postorder(tree):
    if tree is None:
        return

    visit_postorder(tree['left'])
    visit_postorder(tree['right'])
    print(f"Postfix: {tree['value']}")


# Infix/Inorder
def visit_inorder(tree):
    if tree is None:
        return

    visit_inorder(tree['left'])
    print(f"Inorder: {tree['value']}")
    visit_inorder(tree['right'])

if __name__ == "__main__":
    print("Hello binary search :D")

    tree = create_binary_search_tree(50)

    insert_value(tree, 10)
    insert_value(tree, 30)
    insert_value(tree, 2)
    insert_value(tree, 67)
    insert_value(tree, 80)
    insert_value(tree, 51)
    
    print(tree)
    visit_inorder(tree)

