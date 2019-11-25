
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


if __name__ == "__main__":
    print("Hello sort :)")

    lili = [1, 89, 10, 7, 76]

    print(f"Selection sort : {lili} => {selection_sort(lili)}")
    print(f"Insertion sort : {lili} => {insertion_sort(lili)}")