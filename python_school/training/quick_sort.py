# Divide and conquer example
# Diviser pour régner
# Time complexity O(n logn)

import math

def quick_sort(l):
    list_length = len(l)
    if list_length <= 1:
        return l
    
    pivot = l[(list_length - 1) // 2]

    left = [item for item in l if item < pivot]
    right = [item for item in l if item > pivot]

    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)

    return left_sorted + [pivot] + right_sorted


if __name__ == "__main__":
    print("Hello quick_sort")
    list_to_sort = [38, 27, 43, 3, 9, 82, 10]
    print(f"List : {list_to_sort}")
    print(f"List quick sorted : {quick_sort(list_to_sort)}")
    print("\n")
    list_to_sort_b = [1987, 127, 1, 56, 121, 5582, 98, 93, 100]
    print(f"List b : {list_to_sort_b}")
    print(f"List quick sorted b : {quick_sort(list_to_sort_b)}")
