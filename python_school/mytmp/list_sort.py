
def items_min(items):
    if not items:
        return None
    
    res_index = 0
    min_value = items[res_index]
    
    for current_index in range(1, len(items)):
        current_value = items[current_index]
        if current_value < min_value:
            res_index = current_index
            min_value = current_value
    
    return ( res_index, min_value)
        
# Selection sort mutable
def selection_sort(items):

    items_length = len(items)

    if items_length == 0:
        return items

    for i in range(items_length):
        (sub_min_index, _value) = items_min(items[i:items_length])
        min_index = sub_min_index + i
        items[i], items[min_index] = items[min_index], items[i]
    
    return items

# Insertion sort mutable
def insertion_sort(items):
    items_length = len(items)
    
    for i in range(1, items_length):
        current_item = items[i]

        j = i - 1
        while current_item < items[j] and j >= 0:
            items[j + 1] = items[j]
            j -= 1
        
        items[j + 1] = current_item
    
    return items

def merge_list(left, right):

    i = 0
    j = 0

    res_list = []

    while i < len(left) and j < len(right):
        current_left_item = left[i]
        current_right_item = right[j]

        if current_left_item < current_right_item:
            res_list.append(current_left_item)
            i += 1
        else:
            res_list.append(current_right_item)
            j += 1
    

    while i < len(left):
        res_list.append(left[i])
        i += 1
    
    while j < len(right):
        res_list.append(right[j])
        j += 1
    
    return res_list

def merge_sort(items):
    items_length = len(items)

    if items_length == 0 or items_length == 1:
        return items
    
    middle_index = items_length // 2

    left = merge_sort(items[:middle_index])
    right = merge_sort(items[middle_index:])

    return merge_list(left, right)


if __name__ == "__main__":
    print("Hello sort :)")

    lili = [1, 89, 10, 7, 76]

    print(f"Selection sort : {lili} => {selection_sort(lili[:])}")
    print(f"Selection sort : {lili} => {selection_sort(lili[:])}")
    print(f"Merge sort : {lili} => {merge_sort(lili[:])}")