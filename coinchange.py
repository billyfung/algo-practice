# You are given coins of different denominations and a total amount of money amount. Write a function to compute the
# fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# Example 1: coins = [1, 2, 5], amount = 11 return 3 (11 = 5 + 5 + 1) Example 2: coins = [2], amount = 3 return -1


def possible_change(amount, coins):
    if len(coins) == 1:
        if max(coins)<amount:
            return -1
    ways_to_make_n_amount = [0] * (amount + 1)
    ways_to_make_n_amount[0] = 1
    # start from first coin, and build list
    for coin in range(amount+1):
        count = coin
        print "Current coin is:", coin
        for larger_amount in [value for value in coins if value <= coin]:
            # larger amount is the value you want to find number of ways to make with new coin
            # remainder finds how many new ways there are to make amount
            if ways_to_make_n_amount[coin-larger_amount] +1 < count:
                count = ways_to_make_n_amount[coin-larger_amount]+1
            ways_to_make_n_amount[coin] = count
            print ways_to_make_n_amount
    return ways_to_make_n_amount[amount]

print(possible_change(11, [1,2,5]))

#print(possible_change(3,[2]))