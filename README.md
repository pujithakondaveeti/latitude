# Latitude Coding Challenge

## Challenge

Suppose we could access yesterday's stock prices as a list, where:

- The indices are the time in minutes past trade opening time, which was 10:00am local time.
- The values are the price in dollars of the Latitude Financial stock at that time.
- So if the stock cost $5 at 11:00am, stock_prices_yesterday[60] = 5.

Write an efficient function that takes an array of stock prices
and returns the best profit I could have made from
1 purchase and 1 sale of 1 Latitude Financial stock yesterday.

## Solution

1. Iterate through each stock price in the list.
2. If stock price is greater than purchase/buying price, get sold price by taking the max number out of elements excluding adjacent element to purchase_price
3. Else set the purchase_price to current stock_price and continue.

## Assumptions:

- python3.x is installed
- pip is installed
- virtualenv is installed

## How to run the function

```
virtualenv venv
source venv/bin/activate
pip install -r requirements
python max_profit.py 10 7 5 12 11 9
```

## Code Quality

Lint the code using pylint library

```
pylint *.py

Sample output:

pylint *.py
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

```

## Unit Tests

```
pytest -v --no-header
==================================================================================================================== test session starts =====================================================================================================================
collected 4 items

test_get_max_profit.py::test_max_profit_1 PASSED                                                                                                                                                                                                       [ 25%]
test_get_max_profit.py::test_max_profit_2 PASSED                                                                                                                                                                                                       [ 50%]
test_get_max_profit.py::test_max_profit_3 PASSED                                                                                                                                                                                                       [ 75%]
test_get_max_profit.py::test_max_profit_4 PASSED                                                                                                                                                                                                       [100%]

===================================================================================================================== 4 passed in 0.01s ======================================================================================================================

```
