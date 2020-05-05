# TODO: timeit these three


def coin_change_recursive(coins: set, amount: int):
    min_total_coins = amount
    if amount in coins:
        return 1
    else:
        for coin in filter(lambda x: x < amount, coins):
            total_coins = 1 + coin_change_recursive(coins, amount - coin)
            if total_coins < min_total_coins:
                min_total_coins = total_coins
    return min_total_coins


def coin_change_memoized_recursive(coins: set, amount: int, calc_lookup: dict):
    min_total_coins = amount
    if amount in coins:
        calc_lookup[total_change] = 1
        return 1
    elif amount in calc_lookup:
        return calc_lookup[amount]
    else:
        for coin in filter(lambda x: x < amount, coins):
            total_coins = 1 + coin_change_recursive(coins, amount - coin)
            if total_coins < min_total_coins:
                min_total_coins = total_coins
                calc_lookup[total_change] = min_total_coins
    return min_total_coins


def coin_change_dynamic(coins: list, amount: int, min_coins_for_amount: dict):
    for cents in range(amount + 1):
        max_coin_count = cents
        used_coin_val = 1
        for coin_val in filter((lambda x: x < cents), coins):
            if min_coins_for_amount[cents - coin_val] + 1 < max_coin_count:
                max_coin_count = min_coins_for_amount[cents - coin_val] + 1
                used_coin_val = coin_val
        minCoins[cents] = max_coin_count
    return min_coins_for_amount[amount]


# TODO: Move tests and add more
print(coin_change_recursive((1, 5, 10, 25), 26))
print(coin_change_memoized_recursive((1, 5, 10, 25), 22, {}))
print(coin_change_dynamic(coins=(1, 5, 10, 25), amount=63, min_coins_for_amount={}))
