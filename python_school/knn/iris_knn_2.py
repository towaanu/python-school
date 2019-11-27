import pandas
import matplotlib.pyplot as plt
import math

def display_iris(iris_df, unknown_iris):

    setosas = iris_df.query('species == "setosa"')
    versicolors = iris_df.query('species == "versicolor"')
    virginicas = iris_df.query('species == "virginica"')

    plt.scatter(x=setosas["sepal_length"], y=setosas["sepal_width"], color='g', label="Setosas")
    plt.scatter(x=versicolors["sepal_length"], y=versicolors["sepal_width"], color='r', label="Versicolors")
    plt.scatter(x=virginicas["sepal_length"], y=virginicas["sepal_width"], color='b', label="Virginicas")
    plt.scatter(x=unknown_iris[0], y=unknown_iris[1], color='purple', label="???")

    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.legend(loc='upper left')

    plt.savefig("iris_chart.png")

def euclidean_distance(a, b):
    euclidean_sum = 0
    for i in range(len(a)):
        euclidean_sum += (b[i] - a[i])**2
    
    return math.sqrt(euclidean_sum)

def vote(k_items):
    iris_species = set([row[0] for row in k_items])

    max_count = None
    winner = None

    for specie in iris_species:
        count = len([row for row in k_items if row[0] == specie])

        if winner is None or max_count < count:
            max_count = count
            winner = specie
    
    return winner


def knn(data, unknown_data, k):

    sort_data = sorted(data, key=lambda row: euclidean_distance(row[1:], unknown_data))

    k_items = sort_data[:k]

    return (vote(k_items), k_items)

if __name__ == "__main__":
    print("Hello iris :D")

    iris_df = pandas.read_csv("./iris.csv")

    unknown_iris = (5.5, 3.2)
    # unknown_iris = (5.6, 3)
    # unknown_iris = (8, 3)

    display_iris(iris_df, unknown_iris)

    knn_data = [ (row[4], row[0], row[1]) for row in iris_df.values]
    print(knn(knn_data, unknown_iris, 5))

    # print(iris_df)