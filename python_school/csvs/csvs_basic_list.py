import csv

def csv_to_tuple_list(csv_reader):
    return [tuple(row) for row in csv_reader]

def get_index_csv_list(csv_list, key):
    if len(csv_list) == 0 : return None

    index = csv_list[0].index(key)
    return index

def find_elements(csv_list, predicate):
    found_elements = []
    rows = csv_list[1:]
    for row in rows:
        if predicate(row) :
            found_elements.append(row)

    return found_elements        

def sort_csv_list_by_key(csv_list, key):
    key_index = get_index_csv_list(csv_list, key)
    elements = csv_list[1:]
    return sorted(elements, key= lambda row : row[key_index])


if __name__ == "__main__":
    print("Hello csv :D")

    with open("mock_users_20.csv") as csv_users:
        csv_reader = csv.reader(csv_users)
        
        csv_list = csv_to_tuple_list(csv_reader)
        print(csv_list[:5])
        print(sort_csv_list_by_key(csv_list[:4], "first_name"))

        # print(find_elements(csv_list[:5], lambda row: row[4] == "Male"))
       