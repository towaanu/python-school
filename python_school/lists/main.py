import helpers

def simple_find_element(items, elem_to_find):
    found_item = (None, None)

    for i in range(len(items)):
        current_item = items[i]
        if(current_item == elem_to_find):
            found_item = (i, current_item)
            break
    
    return found_item

def find_element(items, predicate):
    found_item = None

    for i in range(len(items)):
        current_item = items[i]
        if(predicate(current_item)):
            found_item = (i, current_item)
            break
    
    return found_item

def max_element(items):
    if items == None or len(items) == 0:
        return None
    
    max_element = items[0]

    for item in items:
        if(item > max_element): 
            max_element = item
    
    return max_element


if __name__ == "__main__":
    items = [21, 1, 4, 78, 2099, 56, 18, 93, 876]

    print(f"Simple Element {simple_find_element(items, 56)}")
    print(f"Find Element {find_element(items, lambda x : x == 56)}")
    print(f"Max Element {max_element(items)}")