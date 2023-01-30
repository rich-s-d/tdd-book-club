

import pytest
import sys
import os
# Add path to src modules.
sys.path.append(os.path.join(sys.path[0][:-5]))
#from franc import Franc
from money import Money, Bank


def test_multiplication():
    #arrange
    five: Money = Money.dollar(5)
    #act
    #assert
    assert Money.dollar(10).equals(five.times(2))
    assert Money.dollar(10).amount == five.times(2).amount
    #act
    #assert
    assert Money.dollar(15).equals(five.times(3))


# Redundant with new code structure (we gutted the subclasses Franc and Dollar.)
# def test_franc_multiplication():
#     #arrange
#     five: Money = Money.franc(5)
#     #act
#     #assert
#     assert Money.franc(10).equals(five.times(2))
#     assert Money.franc(10).amount == five.times(2).amount

#     #act
#     #assert
#     assert Money.franc(15).equals(five.times(3))


def test_equality():
    assert (Money.dollar(5).equals(Money.dollar(5)))
    assert not Money.dollar(5).equals(Money.dollar(6))
    assert not Money.franc(5).equals(Money.dollar(5))


def test_currency():
    assert "USD" == Money.dollar(1).currency()
    assert "CHF" == Money.franc(1).currency()


def test_simple_addition():
    sum = Money.dollar(5).plus(Money.dollar(5)).amount
    assert Money.dollar(10).amount == sum


def test_simple_addition():
    five: Money = Money.dollar(5)
    sum = five.plus(five)
    bank: Bank = Bank()
    reduced: Money = bank.reduce(sum, "USD")
    assert Money.dollar(10).amount == reduced.amount
