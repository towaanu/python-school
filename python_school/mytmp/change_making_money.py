
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

if __name__ == "__main__":
    print("Hello :D")
    money_set = (1, 3, 4)
    amount = 6
    print(f"topdown : {top_down(money_set, amount)}")
    print(f"bottom up : {bottom_up(money_set, amount)}")

