def merge_list(la, lb):
    la_length = len(la)
    lb_length = len(lb)

    i, j = 0, 0

    new_list = []

    while i < la_length and j < lb_length:
        if la[i] < lb[j]:
            new_list.append(la[i])
            i += 1
        else:
            new_list.append(lb[j])
            j += 1

    while i < la_length:
        new_list.append(la[i])
        i += 1

    while j < lb_length:
        new_list.append(lb[j])
        j += 1

    return new_list 


def merge_sort(l):

    list_length = len(l)
    if list_length == 1:
        return l

    middle_index = list_length // 2

    begin_sorted_list = merge_sort(l[:middle_index])
    end_sorted_list = merge_sort(l[middle_index:])

    return merge_list(begin_sorted_list, end_sorted_list)


if __name__ == "__main__":
    print("Hello merge sort :D")

    list_to_sort = [10, 2, 100, 1, 3, 24, 22, 96, 106]
    print(f"List : {list_to_sort}")
    print(f"Merge sorted : {merge_sort(list_to_sort)}")