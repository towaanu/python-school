import math

def greedy_money(amount, money_set):
    sorted_money_set = sorted(money_set)

    res_money = []

    rest_amount = amount
    i = len(sorted_money_set) - 1
    while rest_amount > 0:
        while sorted_money_set[i] > rest_amount and i >= 0:
            i = i - 1

        if i < 0:
            return None


        current_coin = sorted_money_set[i]
        number_of_coin = math.floor(rest_amount / current_coin)
        # Keep 2 decimals
        rest_amount = round(rest_amount % current_coin, 2)
        i = i - 1

        res_money.append((number_of_coin, current_coin))

    return res_money


if __name__ == '__main__':
    euro_money_set = (1, 2, 5, 10, 20, 50, 100, 200, 500)
    euro_amount = 1345
    print(
        f"greedy_money({euro_amount}, {euro_money_set}) : {greedy_money(euro_amount, euro_money_set)} \n")

    real_euro_money_set = (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500)
    euro_cent_amount = 45.34
    print(
        f"greedy_money({euro_cent_amount}, {real_euro_money_set}) : {greedy_money(euro_cent_amount, real_euro_money_set)} \n")
    
    real_euro_money_set = (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500)
    euro_cent_amount = 328.89
    print(
        f"greedy_money({euro_cent_amount}, {real_euro_money_set}) : {greedy_money(euro_cent_amount, real_euro_money_set)} \n")

    not_optimal_money_set = (4, 3, 1)
    amount_b = 6
    print(
        f"greedy_money({amount_b}, {not_optimal_money_set}) : {greedy_money(amount_b, not_optimal_money_set)} \n")
