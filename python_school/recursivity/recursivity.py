def a(n):
    if n == 0:
        return

    print(f"a is called with {n}")
    a(n - 1)
    
    print(f"a is done with {n}")

if __name__ == "__main__":

    print("Graph :D")
    a(5)