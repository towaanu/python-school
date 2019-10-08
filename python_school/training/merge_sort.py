# Divide and conquer example
# Diviser pour régner
# Time complexity O(n logn)

import math

def merge_lists(left, right):
    """ Merge 2 lists preserving order
    The 2 lists needs to be sorted
    >>> merge_lists([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    """
    merged_list = [None] * (len(left) + len(right))

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list[k] = left[i]
            i += 1
        else:
            merged_list[k] = right[j]
            j += 1
        k += 1
    
    for r in range(i, len(left)):
        merged_list[k] = left[r]
        k += 1
    
    for r in range(j, len(right)):
        merged_list[k] = right[r]
        k += 1
    
    return merged_list

def merge_sort(l):
    """ Sort a list using the merge_sort algorithm
    >>> merge_sort([10, 6, 4])
    [4, 6, 10]
    """
    length = len(l)
    if(length == 1):
        return l

    middle_idx = math.ceil(length/2)
    left = merge_sort(l[:middle_idx])
    right = merge_sort(l[middle_idx:])

    return merge_lists(left, right)


if __name__ == "__main__":
    print("Hello merge_sort")
    list_to_sort = [38, 27, 43, 3, 9, 82, 10]
    print(f"List : {list_to_sort}")
    print(f"List merge sorted : {merge_sort(list_to_sort)}")
    print("\n")
    list_to_sort_b = [1987, 127, 1, 56, 121, 5582, 98, 93, 100]
    print(f"List b : {list_to_sort_b}")
    print(f"List merge sorted b : {merge_sort(list_to_sort_b)}")
