def a(n):
    if n == 0:
        return

    print(f"a is called with {n}")
    a(n - 1)
    
    print(f"a is done with {n}")

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_with_print(n):
    print(f"[Factorial enter] {n}")
    if n <= 1:
        print(f"[Factorial return] {n}")
        return 1
    else:
        n_minus_one = factorial_with_print(n - 1)
        print(f"[Factorial return] {n}")
        return n * n_minus_one
    

if __name__ == "__main__":

    print("Graph :D")
    a(5)
    print(f"facto(5) : {factorial(5)}")
    print(f"facto(6) : {factorial_with_print(6)}")