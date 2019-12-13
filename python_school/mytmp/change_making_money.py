
def top_down(money_set, amount, memo={0: 0}):

    if amount in memo:
        return memo[amount]

    if amount < 0:
        return None

    new_nb_coins = None
    nb_coins = None
    for coin in money_set:

        old_nb_coins = top_down(money_set, amount - coin, memo)

        if old_nb_coins is None:
            continue

        new_nb_coins = old_nb_coins + 1

        if nb_coins is None or new_nb_coins < nb_coins:
            nb_coins = new_nb_coins

    memo[amount] = nb_coins
    return memo[amount]


def bottom_up(money_set, amount):
    memo_res = [None for i in range(amount + 1)]
    memo_res[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in money_set:
            old_amount = current_amount - coin

            if old_amount < 0:
                continue

            new_nb_coins = memo_res[old_amount] + 1

            if memo_res[current_amount] is None or new_nb_coins < memo_res[current_amount]:
                memo_res[current_amount] = new_nb_coins

    return memo_res[amount]

# def greedy_money(money_set, amount):
#     rest_amount = amount
#     sorted_money_set = sorted(money_set)
#     res_coins = []

#     while rest_amount > 0:
#         i = len(sorted_money_set) - 1

#         while i >= 0 and sorted_money_set[i] > rest_amount:
#             i -= 1

#         current_money = sorted_money_set[i]

#         nb_coins = rest_amount // current_money
#         rest_amount = rest_amount % current_money
#         res_coins.append((nb_coins, current_money))

#     return res_coins


def greedy_money(money_set, amount):
    rest_amount = amount
    sorted_money_set = sorted(money_set)
    res_coins = []

    i = len(sorted_money_set) - 1

    while rest_amount > 0 and i >= 0:

        current_money = sorted_money_set[i]

        if current_money <= rest_amount:
            nb_coins = rest_amount // current_money
            rest_amount = rest_amount % current_money
            res_coins.append((nb_coins, current_money))

        i -= 1

    # No result found
    if rest_amount > 0:
        return None

    return res_coins


if __name__ == "__main__":
    print("Hello :D")

    ok_money_set = (1, 2, 5, 10, 20, 50)
    ok_amount = 93

    print("-" * 30)
    print(f"Amount: {ok_amount} || Money set {ok_money_set}")
    print(f"topdown : {top_down(ok_money_set, ok_amount)}")
    print(f"bottom up : {bottom_up(ok_money_set, ok_amount)}")
    print(f"greedy_money : {greedy_money(ok_money_set, ok_amount)}")

    money_set = (1, 3, 4)
    amount = 6
    print("-" * 30)
    print(f"Amount: {amount} || Money set {money_set}")
    print(f"topdown : {top_down(money_set, amount)}")
    print(f"bottom up : {bottom_up(money_set, amount)}")
    print(f"greedy_money : {greedy_money(money_set, amount)}")
