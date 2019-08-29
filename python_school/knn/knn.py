import math
import pandas


def euclidean_distance(a, b):
    pow_sum = 0

    for i in range(len(a)):
        pow_sum += (b[i] - a[i]) ** 2

    return math.sqrt(pow_sum)


def k_nearest_neighbors(train_data, data_to_nn, k):
    distance_list = [(euclidean_distance(data_to_nn, row[:-1]),
                      row[len(row) - 1]) for row in train_data]

    sorted_distance_list = sorted(distance_list, key= lambda row : row[0])
    print(sorted_distance_list[:k])



if __name__ == "__main__":
    print("Hello knn :D")
    # dist = euclidean_distance((0, 0), (10, 10))
    # print(dist)
    panda_iris_csv = pandas.read_csv('./iris.csv')
    k_nearest_neighbors(panda_iris_csv.values, (6.4, 3.5, 2.4, 1.2), 5)
    # print(panda_iris_csv.values)
