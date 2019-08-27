import csv

if __name__ == "__main__":
    print("Hello csv :D")

    with open("mock_users_20.csv") as csv_users:
        csv_reader = csv.reader(csv_users)

        for row in csv_reader:
            print(row)
            # print(', '.join(row))