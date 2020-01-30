import functools

def find_max(l):

    if l is None or len(l) == 0:
        return None
    
    max_item = l[0]

    for item in l[1:]:
        if item > max_item:
            max_item = item
    
    return max_item

def compute_avg(l):
    l_sum = 0
    for item in l:
        l_sum += item
    
    return l_sum / len(l)

def compute_avg_reduce(l):
    l_sum = functools.reduce(lambda current_sum, item: current_sum + item, l)
    return l_sum / len(l)

if __name__ == "__main__":
    print("Hello")
    list_a = [1, 10, 40, 5, 8, 21]

    print(f"Avg: {compute_avg(list_a)}")
    print(f"Avg ( reduce ): {compute_avg_reduce(list_a)}")
    print(f"Find max: {find_max(list_a)}")