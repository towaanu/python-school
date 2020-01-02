def top_down_money(money_set, amount, memo=None, amount_path=None):

    if memo is None:
        memo = {0: 0}
    
    if amount_path is None:
        amount_path = {0: 0}

    if amount < 0:
        return (None, None)
    
    if amount in memo:
        return (memo[amount], amount_path)
    
    res_nb_coins = None
    best_coin = None
    for coin in money_set:
        (nb_coins, _) = top_down_money(money_set, amount - coin, memo, amount_path)

        if nb_coins is None:
            continue

        nb_coins += 1

        if res_nb_coins is None:
            res_nb_coins = nb_coins
            best_coin = coin
        else:
            # Take the minimum
            if nb_coins < res_nb_coins:
                res_nb_coins = nb_coins
                best_coin = coin

    amount_path[amount] = amount - best_coin
    memo[amount] = res_nb_coins
    return (res_nb_coins, amount_path)

def bottom_up_money(money_set, amount):
    if amount < 0:
        return None

    res_coins = [0]
    
    for current_amount in range(1, amount + 1):
        nb_coin = None
        res_nb_coin = None
        for coin in money_set:
            new_amount = current_amount - coin

            if new_amount < 0:
                continue
            
            nb_coin = res_coins[new_amount] + 1

            if res_nb_coin is None or nb_coin < res_nb_coin:
                res_nb_coin = nb_coin

        res_coins.append(res_nb_coin)

    return (res_coins[amount], res_coins)

if __name__ == "__main__":
    print("Hello tmp exo")

    euro_money_set = {1, 2, 5, 10, 20}
    amount = 28

    other_money_set = {1, 3, 4}
    other_amount = 6

    print(f"Euro money set => 28 : {top_down_money(euro_money_set, amount)}")
    print(f"Euro money set => 28 : {bottom_up_money(euro_money_set, amount)}")

    print(f"Other money set => 6 : {top_down_money(other_money_set, other_amount)}")
    print(f"Other money set => 6 : {bottom_up_money(other_money_set, other_amount)}")