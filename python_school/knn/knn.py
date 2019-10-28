import math
import pandas
import matplotlib.pyplot as plt

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

def k_nearest_neighbors_petal(train_data, data_to_nn, k):
    distance_list = [(euclidean_distance((data_to_nn[2], data_to_nn[3]), (row[2], row[3])),
                      row[len(row) - 1]) for row in train_data]

    sorted_distance_list = sorted(distance_list, key= lambda row : row[0])
    print(sorted_distance_list[:k])

def show_iris_plot(iris_dataframe, search_point):
    setosas = iris_dataframe.query('species == "setosa"')
    versicolors = iris_dataframe.query('species == "versicolor"')
    virginicas = iris_dataframe.query('species == "virginica"')

    plt.scatter(setosas['petal_length'], setosas['petal_width'], color='g', label="setosa")
    plt.scatter(versicolors['petal_length'], versicolors['petal_width'], color='b', label="versicolor")
    plt.scatter(virginicas['petal_length'], virginicas['petal_width'], color='r', label="virginica")

    plt.scatter(search_point[2], search_point[3], color='purple', label="???")

    plt.legend()
    plt.savefig('scatter_plot.png')
    plt.clf()

if __name__ == "__main__":
    print("Hello knn :D")
    # dist = euclidean_distance((0, 0), (10, 10))
    # print(dist)
    panda_iris_csv = pandas.read_csv('./iris.csv')

    search_point = (6.4, 3.5, 2.4, 1.2)
    # k_nearest_neighbors(panda_iris_csv.values, search_point, 5)
    k_nearest_neighbors_petal(panda_iris_csv.values, search_point, 5)
    show_iris_plot(panda_iris_csv, search_point)

    # print(panda_iris_csv.values)
