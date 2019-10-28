import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Hello plot")
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.savefig('foo.png')
    # plt.show()