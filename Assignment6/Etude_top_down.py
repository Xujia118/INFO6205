def min_change(amount, coins):
    ans, coins_used = _min_change(amount, coins, {})
    return -1 if ans == float('inf') else (ans, coins_used)

def _min_change(amount, coins, memo):
    if amount in memo:
        return memo[amount]

    if amount < 0:
        return float('inf'), []

    if amount == 0:
        return 0, []

    min_coins = float('inf')
    chosen_coins = []

    for coin in coins:
        coins_count, coins_used = _min_change(amount - coin, coins, memo)
        coins_count += 1

        if coins_count < min_coins:
            min_coins = coins_count
            chosen_coins = [coin] + coins_used

    memo[amount] = min_coins, chosen_coins
    return min_coins, chosen_coins

amount = 102
coins = [1, 5, 10, 25]
min_coins, coins_used = min_change(amount, coins)
if min_coins != -1:
    print(f"Minimum number of coins needed: {min_coins}")
    print("Coins used:", coins_used)
else:
    print("It's not possible to make change for the given amount.")