# Using dynamic programming for the change making problem ( probleme de rendu de monnaie)
# O(A*C)
# Maison :D
import math

def change_making_problem(money_set, amount, memo={}):
    # We need 0 coin to get to 0
    memo[0] = 0

    if amount in memo:
        return memo[amount]

    if amount < 0:
        return math.inf

    nb_coins = None

    for coin in money_set:
        new_nb_coins = change_making_problem(money_set, amount - coin, memo) + 1

        if nb_coins is None or new_nb_coins < nb_coins:
            nb_coins = new_nb_coins

    memo[amount] = nb_coins

    return nb_coins

def change_making_problem_bottom_up(money_set, amount):
    results_memo = {}
    results_memo[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in money_set:
            old_amount = current_amount - coin

            if old_amount in results_memo:
                nb_coin = results_memo[old_amount] + 1
                if current_amount not in results_memo or results_memo[current_amount] > nb_coin:
                    results_memo[current_amount] = nb_coin

    return results_memo[amount]



if __name__ == "__main__":

    print("Hello change home :D")

    coins = [1, 2, 5]
    amount = 20

    print(f"Top down : {change_making_problem(coins, amount)}")
    print(f"Bottom up : {change_making_problem_bottom_up(coins, amount)}")

    # not_optimal_money_set = (4, 3, 1)
    not_optimal_money_set = (1, 3, 4)
    amount_b = 6

    print(
        f"Bottom up: {change_making_problem_bottom_up(not_optimal_money_set, amount_b)}")
    print(
        f"Top down ?: {change_making_problem(not_optimal_money_set, amount_b)}")
