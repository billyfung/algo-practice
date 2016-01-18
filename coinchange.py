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
    for coin in coins:
        print "Current coin is:", coin
        for larger_amount in xrange(coin, amount+1):
            # larger amount is the value you want to find number of ways to make with new coin
            print "Larger amount is:", larger_amount
            # remainder finds how many new ways there are to make amount
            larger_amount_remainder = larger_amount - coin
            print "Remainder amount:",larger_amount_remainder
            # so to find newer ways to make amount, we use the remainder to find old calculated amounts
            # ex. amount = 3, we know to make 3 we can use 3x1coin, or 1x2coin + 2x1coin
            # so our approach to start from finding all ways_to_make_n_amounts with nx1coin, we already know that number
            ways_to_make_n_amount[larger_amount] += ways_to_make_n_amount[larger_amount_remainder]
            print ways_to_make_n_amount
    return ways_to_make_n_amount[amount]

print(possible_change(11, [1,2,5]))
# Current coin is: 1
# Larger amount is: 1
# Remainder amount: 0
# [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Larger amount is: 2
# Remainder amount: 1
# [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Larger amount is: 3
# Remainder amount: 2
# [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# Larger amount is: 4
# Remainder amount: 3
# [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
# Larger amount is: 5
# Remainder amount: 4
# [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# Larger amount is: 6
# Remainder amount: 5
# [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
# Larger amount is: 7
# Remainder amount: 6
# [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
# Larger amount is: 8
# Remainder amount: 7
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
# Larger amount is: 9
# Remainder amount: 8
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
# Larger amount is: 10
# Remainder amount: 9
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
# Larger amount is: 11
# Remainder amount: 10
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Current coin is: 2
# Larger amount is: 2
# Remainder amount: 0
# [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Larger amount is: 3
# Remainder amount: 1
# [1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
# Larger amount is: 4
# Remainder amount: 2
# [1, 1, 2, 2, 3, 1, 1, 1, 1, 1, 1, 1]
# Larger amount is: 5
# Remainder amount: 3
# [1, 1, 2, 2, 3, 3, 1, 1, 1, 1, 1, 1]
# Larger amount is: 6
# Remainder amount: 4
# [1, 1, 2, 2, 3, 3, 4, 1, 1, 1, 1, 1]
# Larger amount is: 7
# Remainder amount: 5
# [1, 1, 2, 2, 3, 3, 4, 4, 1, 1, 1, 1]
# Larger amount is: 8
# Remainder amount: 6
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 1, 1, 1]
# Larger amount is: 9
# Remainder amount: 7
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1]
# Larger amount is: 10
# Remainder amount: 8
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 1]
# Larger amount is: 11
# Remainder amount: 9
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
# Current coin is: 5
# Larger amount is: 5
# Remainder amount: 0
# [1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6]
# Larger amount is: 6
# Remainder amount: 1
# [1, 1, 2, 2, 3, 4, 5, 4, 5, 5, 6, 6]
# Larger amount is: 7
# Remainder amount: 2
# [1, 1, 2, 2, 3, 4, 5, 6, 5, 5, 6, 6]
# Larger amount is: 8
# Remainder amount: 3
# [1, 1, 2, 2, 3, 4, 5, 6, 7, 5, 6, 6]
# Larger amount is: 9
# Remainder amount: 4
# [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 6, 6]
# Larger amount is: 10
# Remainder amount: 5
# [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10, 6]
# Larger amount is: 11
# Remainder amount: 6
# [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10, 11]

print(possible_change(3,[2]))