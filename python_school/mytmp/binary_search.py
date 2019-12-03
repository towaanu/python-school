def binary_search_recursive(l, search_item):
    l_length = len(l)

    if l_length == 0:
        return None

    middle_index = l_length // 2
    middle_item = l[middle_index]

    if search_item == middle_item:
        return middle_index
    
    if search_item > middle_item:
        new_begin_index = middle_index + 1
        # middle_index to return the global index and not the sub index of binary_search
        res_index = binary_search_recursive(l[new_begin_index:], search_item)
        if res_index is None:
            return None
        else:
            return new_begin_index + binary_search_recursive(l[new_begin_index:], search_item)

    if search_item < middle_item:
        return binary_search_recursive(l[:middle_index], search_item)

def binary_search(l, search_item):
    l_length = len(l)

    if l_length == 0:
        return None

    begin_index = 0
    last_index = l_length - 1

    current_item = None
    res_index = None

    while begin_index <= last_index and res_index is None:
        current_index = (begin_index + last_index) // 2

        current_item = l[current_index]

        if search_item < current_item :
            last_index = current_index - 1
        elif search_item > current_item:
            begin_index = current_index + 1
        else: 
            res_index = current_index
    
    return res_index



if __name__ == "__main__":
    print("Hello tmp binary search :D")

    sorted_list = [3, 10, 15, 20, 110, 542]

    a = 1
    b = 15
    c = 20
    d = 600
    e = 110

    print(f"binary_search_recursive({sorted_list, a}) = {binary_search_recursive(sorted_list, a)}")
    print(f"binary_search({sorted_list}, {a}) = {binary_search(sorted_list, a)} \n")

    print(f"binary_search_recursive({sorted_list}, {b}) = {binary_search_recursive(sorted_list, b)}")
    print(f"binary_search({sorted_list}, {b}) = {binary_search(sorted_list, b)} \n")

    print(f"binary_search_recursive({sorted_list}, {c}) = {binary_search_recursive(sorted_list, c)}")
    print(f"binary_search({sorted_list}, {c}) = {binary_search(sorted_list, c)} \n")

    print(f"binary_search_recursive({sorted_list}, {d}) = {binary_search_recursive(sorted_list, d)}")
    print(f"binary_search({sorted_list}, {d}) = {binary_search(sorted_list, d)} \n")

    print(f"binary_search_recursive({sorted_list}, {e}) = {binary_search_recursive(sorted_list, e)}")
    print(f"binary_search({sorted_list}, {e}) = {binary_search(sorted_list, e)} \n")

    