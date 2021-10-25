"""
Latitude coding challenge Unit Tests.

Author:
    Pujitha Kondaveeti
Version: 1.0.0

Changelog:
    25-Oct-2021 -   Initial commit
"""

from max_profit import get_max_profit


def test_max_profit_1():
    """Asserts the max profit from array of share prices by ignoring adjacent time step"""
    assert get_max_profit([10, 7, 5, 12, 11, 9]) == 6


def test_max_profit_2():
    """Asserts the max profit from array of share prices by ignoring adjacent time step"""
    assert get_max_profit(
        [30, 28, 26, 17, 11, 3, 23, 8, 12, 11, 15, 6, 16, 14]) == 13


def test_max_profit_3():
    """
        Negative Scenario:
        Asserts -1 when there is no profit
    """
    assert get_max_profit([30, 28, 26, 6, 1]) == -1


def test_max_profit_4():
    """
        Negative Scenario:
        Asserts -1 when the input contains less than 3 elements because it requires
        atleast 3 elements to buy and sell a non adjacent stock
    """
    assert get_max_profit([2, 4]) == -1
