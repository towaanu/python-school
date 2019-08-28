import pandas


if __name__ == "__main__":
    print("Hello csv pandas :D")

    panda_csv = pandas.read_csv('./mock_users_20.csv')

    res_data = panda_csv.query('gender == "Female"').sort_values(by=['first_name'])

    print(res_data)
