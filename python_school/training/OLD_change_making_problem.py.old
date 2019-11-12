# Using dynamic programming for the change making problem ( probleme de rendu de monnaie)
# O(A*C)
import math

def cmp_bottom_up(coins, amount):
    change_solutions = [amount + 1 for _ in range(amount + 1)]

    change_solutions[0] = 0

    for amount in range(1, amount + 1):
        for coin in coins:
            new_amount = amount - coin

            if new_amount >= 0:
                new_solution = change_solutions[new_amount] + 1
                current_solution = change_solutions[amount]
                change_solutions[amount] = min(new_solution, current_solution)
    
    return change_solutions


def cmp_top_down(coins, amount):
    if amount < 0:
        return 0

    change_solutions = [None for _ in range(amount + 1)]
    change_solutions[0] = 0
    return cmp_top_down_recursive(coins, amount, change_solutions)

def cmp_top_down_recursive(coins, amount, change_solutions):
    if amount < 0:
        return -1

    if amount == 0:
        return 0
    
    if change_solutions[amount] is not None:
        return change_solutions[amount]
    
    minimum = math.inf

    for coin in coins:
        change_result = cmp_top_down_recursive(coins, amount - coin, change_solutions)
        
        if change_result >= 0 and change_result < minimum:
            minimum = 1 + change_result

    change_solutions[amount] = -1 if minimum == math.inf else minimum
    
    return change_solutions[amount]

if __name__ == "__main__":
    
    print("Hello change :D")

    coins = [1, 2, 5]
    amount = 20

    print(f"Bottom up : {cmp_bottom_up(coins, amount)}")
    print(f"Top down : {cmp_top_down(coins, amount)}")

    not_optimal_money_set = (4, 3, 1)
    amount_b = 6

    print(f"Bottom up ?: {cmp_bottom_up(not_optimal_money_set, amount_b)}")
    print(f"Top down ?: {cmp_top_down(not_optimal_money_set, amount_b)}")