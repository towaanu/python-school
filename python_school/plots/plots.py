import matplotlib.pyplot as plt

def make_basic_plot():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.savefig('basic_plot.png')
    plt.clf()

def make_scatter_plot():
    xs = [1, 2, 3, 4]
    ys = [1, 2, 3, 4]
    # fig, ax = plt.subplots()
    plt.scatter(xs, ys, color='g', label="foo")
    plt.legend()
    plt.savefig('scatter_plot.png')
    plt.clf()

if __name__ == "__main__":
    print("Hello plot")
    make_basic_plot()
    make_scatter_plot()
    # plt.show()