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

def compute_avg(items):
    if(items == None or len(items) == 0):
        return None
    
    items_sum = 0
    for item in items:
        items_sum += item
    
    items_avg = items_sum/len(items)
    return items_avg

def simple_min_element(items):
    if(items is None or len(items) == 0):
        return None
    
    min_item = items[0]

    for item in items[1:]:
        if(item < min_item): 
            min_item = item

    return min_item

def min_element(items):
    if(items is None or len(items) == 0):
        return None
    
    min_item = (0, items[0])

    for i in range(1, len(items)):
        current_item = items[i]
        _index, min_item_value = min_item
        if(current_item < min_item_value): 
            min_item = (i, current_item)

    return min_item

def selection_sort(items):
    sorted_list = list(items)
    for i in range(len(sorted_list)):
        min_index, _value = min_element(sorted_list[i:])

        sorted_list_min_index = min_index + i

        # swap value
        sorted_list[i], sorted_list[sorted_list_min_index] = sorted_list[sorted_list_min_index], sorted_list[i]
    
    return sorted_list

def insertion_sort(items):
    sorted_list = list(items)
    for i in range(1, len(sorted_list)):
        current_item = sorted_list[i]
        j = i - 1
        while(j >= 0 and current_item < sorted_list[j]):
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j+1] = current_item
        
    
    return sorted_list



if __name__ == "__main__":
    items = [521, 134, 78, 2099, 56, 18, 1, 93, 876]

    print(f"Items : {helpers.display_list_str(items)}")
    print(f"Simple Element {simple_find_element(items, 56)}")
    print(f"Find Element {find_element(items, lambda x : x == 56)}")
    print(f"Max Element {max_element(items)}")
    print(f"Min Element {min_element(items)}")
    print(f"Average Element {compute_avg(items)}")

    selection_sort_list = selection_sort(items)
    print(f"Selection sort {helpers.display_list_str(selection_sort_list)}")

    insertion_sort_list = insertion_sort(items)
    print(f"Insertion sort {helpers.display_list_str(insertion_sort_list)}")
