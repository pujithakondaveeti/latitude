"""
Latitude coding challenge.

Author:
    Pujitha Kondaveeti
Version: 1.0.0

Example:
    stock_prices_yesterday = [10, 7, 5, 12, 11, 9];
    get_max_profit(stock_prices_yesterday)
    # returns 6 (buying for $5 and selling for $11)
Changelog:
    25-Oct-2021 -   Initial commit
"""

import argparse
import sys


def get_max_profit(stock_prices_yesterday):
    """
    Takes in an array of stock prices
    and returns the best profit I could have made from
    1 purchase and 1 sale of 1 Latitude Financial stock yesterday.
    You must buy before you sell.
    You may not buy and sell in adjacent time step
    (i.e. > 1 minute at a minimum must pass between the purchase and sale).
    """
    # Start by assuming first element is the purchase price and sold price is zero
    purchase_price = stock_prices_yesterday[0]
    sold_price = 0
    max_profit = -1
    arr_length = len(stock_prices_yesterday)

    # loop through stock prices list
    try:
        for i, stock_price in enumerate(stock_prices_yesterday):
            # If stock price is greater than purchase/buying price (Sell!!!)
            # Get sold price by taking the max number out of elements excluding
            # adjacent element to purchase_price

            if (i + 2) <= arr_length and stock_price > purchase_price:
                sold_price = max(stock_prices_yesterday[(
                    stock_prices_yesterday.index(purchase_price) + 2):])
                current_profit = sold_price - purchase_price
                # If current_profit is greater than existing max_profit, set it to max_profit
                max_profit = max(max_profit, current_profit)

            # Else set the purchase_price to current stock_price and continue
            else:
                purchase_price = stock_price
    except ReferenceError as err:
        print("Exception while getting maximu share price! ", err)

    return max_profit


if __name__ == '__main__':
    #Start here and validate input parameters.

    parser = argparse.ArgumentParser(description='Parse input arguments.')
    parser.add_argument('-s',
                        '--stock-prices',
                        metavar='N',
                        nargs="*",
                        type=int,
                        help='Stock prices argument is required',
                        required=True)
    args = parser.parse_args()

    stock_prices = args.stock_prices
    if not stock_prices:
        parser.print_help()
        sys.exit()

    if not len(stock_prices) > 2:
        sys.exit("Stock prices for a minimum 3 time steps has to be supplied!")

    profit = get_max_profit(stock_prices)

    if profit < 0:
        sys.exit("No profit could be made with the given stock prices!!!")

    print(get_max_profit(stock_prices))
