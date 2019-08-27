import csv

def csv_to_dict_list(csv_reader):
    csv_reader_list = list(csv_reader)
    headers = csv_reader_list[0]
    rows = csv_reader_list[1:]
    dict_list = []

    for row in rows:
        tuple_row = []
        for i in range(len(headers)):
            key = headers[i]
            value = row[i]
            tuple_row.append((key, value))

        dict_row = dict(tuple_row) 
        dict_list.append(dict_row)

    return dict_list
    
def find_elements(csv_list, predicate):
    found_elements = []
    rows = csv_list[1:]
    for row in rows:
        if predicate(row) :
            found_elements.append(row)

    return found_elements        

def sort_csv_list_by_key(csv_list, key):
    elements = csv_list[1:]
    return sorted(elements, key= lambda row : row[key])


if __name__ == "__main__":
    print("Hello csv dict :D")

    with open("mock_users_20.csv") as csv_users:
        csv_reader = csv.reader(csv_users)
        
        csv_list = csv_to_dict_list(csv_reader)
        print(find_elements(csv_list, lambda row : row['gender'] == 'Female'))
        print(sort_csv_list_by_key(csv_list, "last_name"))