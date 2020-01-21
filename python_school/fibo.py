import time

def fibo(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fibo(n - 1) + fibo (n - 2)

def fibo_memo(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fibo_memo(n - 1, memo) + fibo_memo(n - 2, memo)

    return memo[n]

def fibo_loop_memo(n):
    fibo_numbers = [0, 1]
    for i in range(2, n + 1):
        new_fibo_number = fibo_numbers[i - 1] + fibo_numbers[i - 2]
        fibo_numbers.append(new_fibo_number)
    
    return fibo_numbers[n]


if __name__ == "__main__":
    print("Hello fibo")

    n = 32

    start_fibo_time = time.time()
    res_fibo = fibo(n)
    fibo_time = time.time() - start_fibo_time
    print(f"fibo({n}) = {res_fibo} in {fibo_time} seconds")

    start_fibo_memo_time = time.time()
    res_fibo_memo = fibo_memo(n)
    time_fibo_memo = time.time() - start_fibo_memo_time
    print(f"fibo_memo({n}) = {res_fibo_memo} in {time_fibo_memo} seconds")

    start_fibo_loop_memo_time = time.time()
    res_fibo_loop_memo = fibo_loop_memo(n)
    time_fibo_loop_memo = time.time() - start_fibo_loop_memo_time
    print(f"fibo_loop_memo({n}) = {res_fibo_loop_memo} in {time_fibo_loop_memo} seconds")
    