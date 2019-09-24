from queue import Queue

# def insert_value(tree, value):

#     if tree is None:
#         return {'value': value, 'left': None, 'right': None}

#     if value < tree['value']:
#         return insert_value(tree['left'], value)
#     elif value > tree['value']:
#         return insert_value(tree['right'], value)
#     else:
#         return None


def insert_value(tree, value):

    if value < tree['value']:
        if tree['left'] is None:
            tree['left'] = {'value': value, 'left': None, 'right': None}
        return insert_value(tree['left'], value)

    elif value > tree['value']:
        if tree['right'] is None:
            tree['right'] = {'value': value, 'left': None, 'right': None}
        return insert_value(tree['right'], value)

    else:
        return None

def search_value(tree, value):
    if tree == None:
        return None
    
    if value < tree['value']:
        return search_value(tree['left'], value)
    elif value > tree['value']:
        return search_value(tree['right'], value)
    else:
        return tree # found it !

def breadth_first_search(tree):
    nodes_to_visit = Queue()
    nodes_to_visit.put(tree)

    while not nodes_to_visit.empty():
        current_node = nodes_to_visit.get()

        if current_node['left'] is not None:
            nodes_to_visit.put(current_node['left'])
        
        if current_node['right'] is not None:
            nodes_to_visit.put(current_node['right'])
        
        print(f"{current_node['value']}")


if __name__ == "__main__":
    print("Hello bst :D")

    my_bst = {
        'value': 50,
        'left': {'value': 20, 'left': None, 'right': None},
        'right': {'value': 60, 'left': None, 'right': None}
    }

    insert_value(my_bst, 30)
    insert_value(my_bst, 18)
    insert_value(my_bst, 130)
    insert_value(my_bst, 51)
    insert_value(my_bst, 200)
    breadth_first_search(my_bst)

    print(search_value(my_bst, 51))
    print(search_value(my_bst, 18))
    print(search_value(my_bst, 200))
    print(search_value(my_bst, 22))
