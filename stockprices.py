# have input of stock prices in list
# indices are the time in minutes past trade opening time, which was 9:30am local time
# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500
# write function to take list and output best profit
# ex. stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
# get_max_profit(stock_prices_yesterday)= 6, (buying for $5 and selling for $11)


def get_max_profit(stock_prices):
    # we want to find the max price and the min price in the list
    # highest price must come after lowest price
    # negative profit happens if price decreases all day
    highest_price = max(stock_prices)
    lowest_price = min(stock_prices)
    if len(stock_prices)<2:
        raise IndexError('Need at least 2 prices')
    # first check the easy case
    if stock_prices.index(highest_price)>stock_prices.index(lowest_price):
        max_profit = highest_price-lowest_price
    else:
        # start with the first price as lowest
        lowest_price = stock_prices[0]
        max_profit = stock_prices[1] - stock_prices[0]
        for current_price in stock_prices:
            # iterate through all prices and keep track of highest profit
            # compare with previous max profit
            if stock_prices.index(lowest_price) == 0:
                continue
            maybe_profit = current_price-lowest_price
            max_profit = max(maybe_profit, max_profit)
    # edge cases! what if the stock decreases only?? return negative profit to minimize loss
    return max_profit


stock_prices_yesterday = [10, 9, 4, 5, 1]
print(get_max_profit(stock_prices_yesterday))
